"""Casos de uso de inventario y consultas del concesionario.

Ejemplo:
    >>> # Se instancia con un Concesionario y se llama a sus metodos.
"""

from src.entities.coche_combustion import CocheCombustion
from src.entities.coche_electrico import CocheElectrico
from src.entities.coche_hibrido import CocheHibrido
from src.entities.coche import Coche
from src.entities.resultado import Resultado


class GestionConcesionarioService:
    """Orquesta operaciones de inventario y consulta."""

    def __init__(self, concesionario):
        self._concesionario = concesionario

    def incorporar_coche(self, coche):
        """Incorpora un coche al inventario."""
        return self._concesionario.agregar_coche(coche)

    def alta_coche(self, tipo, matricula, marca):
        """Crea un coche por tipo y lo incorpora al inventario."""
        tipo_normalizado = str(tipo).strip().lower()
        if tipo_normalizado == "combustion":
            coche = CocheCombustion(matricula, marca)
        elif tipo_normalizado == "electrico":
            coche = CocheElectrico(matricula, marca)
        elif tipo_normalizado == "hibrido":
            coche = CocheHibrido(matricula, marca)
        else:
            return Resultado.error("Tipo de coche no valido", "TIPO_NO_VALIDO")

        return self.incorporar_coche(coche)

    def retirar_coche(self, coche):
        """Retira un coche del inventario."""
        return self._concesionario.eliminar_coche(coche)

    def baja_coche_por_matricula(self, matricula):
        """Retira un coche localizandolo por matrícula."""
        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        propietario = self._concesionario.buscar_propietario_por_matricula(matricula)
        if propietario is not None:
            return Resultado.error(
                (
                    f"La matricula {matricula} esta asociada al cliente con DNI "
                    f"{propietario.dni}. Debe retirarse la asociacion antes de la baja."
                ),
                "COCHE_ASOCIADO",
            )

        return self._concesionario.eliminar_coche(coche)

    def modificar_coche(self, matricula, nueva_marca):
        """Modifica la marca manteniendo identidad y estado técnico del coche."""
        coche_actual = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche_actual is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        coche_actualizado = self._crear_copia_coche(coche_actual, nueva_marca)
        return self._concesionario.sustituir_coche(coche_actualizado)

    def avanzar_coche_por_matricula(self, matricula, km):
        """Hace avanzar un coche del inventario localizándolo por matrícula."""
        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        return coche.avanzar(km)

    def obtener_info_avance_por_matricula(self, matricula):
        """Devuelve energía, consumo y km máximos de avance para la UI."""
        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        if isinstance(coche, CocheHibrido):
            detalle_electrico = {
                "fuente": "electrico",
                "energia_disponible": coche.bateria_kwh,
                "unidad_energia": "kWh",
                "consumo_por_km": CocheElectrico.CONSUMO_KWH_POR_KM,
                "unidad_consumo": "kWh/km",
                "km_maximos": coche.bateria_kwh / CocheElectrico.CONSUMO_KWH_POR_KM,
            }
            detalle_gasolina = {
                "fuente": "gasolina",
                "energia_disponible": coche.gasolina,
                "unidad_energia": "L",
                "consumo_por_km": CocheCombustion.CONSUMO_LITROS_POR_KM,
                "unidad_consumo": "L/km",
                "km_maximos": coche.gasolina / CocheCombustion.CONSUMO_LITROS_POR_KM,
            }
            km_maximos = max(detalle_electrico["km_maximos"], detalle_gasolina["km_maximos"])
            return Resultado.exito(
                "Informacion de avance obtenida",
                valor={
                    "matricula": coche.matricula,
                    "tipo": coche.__class__.__name__,
                    "detalles": [detalle_electrico, detalle_gasolina],
                    "km_maximos": km_maximos,
                },
            )

        if isinstance(coche, CocheCombustion):
            consumo = CocheCombustion.CONSUMO_LITROS_POR_KM
            km_maximos = coche.gasolina / consumo
            return Resultado.exito(
                "Informacion de avance obtenida",
                valor={
                    "matricula": coche.matricula,
                    "tipo": coche.__class__.__name__,
                    "detalles": [
                        {
                            "fuente": "gasolina",
                            "energia_disponible": coche.gasolina,
                            "unidad_energia": "L",
                            "consumo_por_km": consumo,
                            "unidad_consumo": "L/km",
                            "km_maximos": km_maximos,
                        }
                    ],
                    "km_maximos": km_maximos,
                },
            )

        if isinstance(coche, CocheElectrico):
            consumo = CocheElectrico.CONSUMO_KWH_POR_KM
            km_maximos = coche.bateria_kwh / consumo
            return Resultado.exito(
                "Informacion de avance obtenida",
                valor={
                    "matricula": coche.matricula,
                    "tipo": coche.__class__.__name__,
                    "detalles": [
                        {
                            "fuente": "electrico",
                            "energia_disponible": coche.bateria_kwh,
                            "unidad_energia": "kWh",
                            "consumo_por_km": consumo,
                            "unidad_consumo": "kWh/km",
                            "km_maximos": km_maximos,
                        }
                    ],
                    "km_maximos": km_maximos,
                },
            )

        return Resultado.error("Tipo de coche no compatible", "TIPO_NO_COMPATIBLE")

    def obtener_tipo_coche_por_matricula(self, matricula):
        """Devuelve el tipo de coche para guiar formularios de la UI."""
        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        return Resultado.exito("Tipo de coche encontrado", valor=coche.__class__.__name__)

    def cargar_energia_coche_por_matricula(self, matricula, litros=None, kwh=None):
        """Reposta/recarga un coche según su tipo, usando matrícula."""
        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")

        if isinstance(coche, CocheHibrido):
            resultado_gasolina = coche.repostar(litros)
            if not resultado_gasolina.ok:
                return resultado_gasolina

            resultado_bateria = coche.recargar(kwh)
            if not resultado_bateria.ok:
                return resultado_bateria

            return Resultado.exito(
                "Repostaje y recarga completados",
                valor={"gasolina": coche.gasolina, "bateria_kwh": coche.bateria_kwh},
            )

        if isinstance(coche, CocheCombustion):
            return coche.repostar(litros)

        if isinstance(coche, CocheElectrico):
            return coche.recargar(kwh)

        return Resultado.error("Tipo de coche no compatible", "TIPO_NO_COMPATIBLE")

    def buscar_cliente(self, dni):
        """Busca un cliente por DNI."""
        return self._concesionario.buscar_cliente_por_dni(dni)

    def listar_coches_con_cliente(self):
        """Devuelve una vista simple de coches para mostrar en la UI."""
        filas = []
        for coche in self._concesionario.coches:
            propietario = self._concesionario.buscar_propietario_por_matricula(coche.matricula)
            filas.append(
                {
                    "matricula": coche.matricula,
                    "marca": coche.marca,
                    "tipo": coche.__class__.__name__,
                    "dni_propietario": propietario.dni if propietario else None,
                }
            )
        return filas

    def listar_kilometros_por_marca(self):
        """Devuelve una vista ordenada de kilómetros acumulados por marca."""
        acumulados = Coche.listar_kilometros_por_marca()
        filas = []
        for marca in sorted(acumulados):
            filas.append({"marca": marca, "kilometros": acumulados[marca]})
        return filas

    def resumen(self):
        """Devuelve un resumen util para UI."""
        return {
            "nombre": self._concesionario.nombre,
            "num_clientes": len(self._concesionario.clientes),
            "num_coches": len(self._concesionario),
        }

    @staticmethod
    def _crear_copia_coche(coche, nueva_marca):
        if isinstance(coche, CocheHibrido):
            return CocheHibrido(
                coche.matricula,
                nueva_marca,
                bateria_kwh=coche.bateria_kwh,
                gasolina=coche.gasolina,
                kilometros_recorridos=coche.kilometros_recorridos,
            )
        if isinstance(coche, CocheElectrico):
            return CocheElectrico(
                coche.matricula,
                nueva_marca,
                bateria_kwh=coche.bateria_kwh,
                kilometros_recorridos=coche.kilometros_recorridos,
            )
        if isinstance(coche, CocheCombustion):
            return CocheCombustion(
                coche.matricula,
                nueva_marca,
                gasolina=coche.gasolina,
                kilometros_recorridos=coche.kilometros_recorridos,
            )

        return coche

