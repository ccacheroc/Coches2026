"""Casos de uso de gestion de personas.

Ejemplo:
    >>> # Se instancia con un Concesionario y se llama a sus metodos.
"""

from src.entities.persona import Persona
from src.entities.resultado import Resultado


class GestionPersonasService:
    """Orquesta operaciones entre clientes del concesionario."""

    def __init__(self, concesionario):
        self._concesionario = concesionario

    def alta_cliente(self, dni, nombre, apellido, matricula=None):
        """Da de alta un cliente y opcionalmente le asocia un coche libre."""
        persona = Persona(dni, nombre, apellido)
        asignacion = self._asignar_coche_si_procede(persona, matricula)
        if not asignacion.ok:
            return asignacion

        return self._concesionario.anadir_cliente(persona)

    def modificar_cliente(self, dni, nombre, apellido, matricula=None):
        """Modifica nombre, apellido y coche asociado de un cliente existente."""
        cliente_actual = self._concesionario.buscar_cliente_por_dni(dni)
        if cliente_actual is None:
            return Resultado.error("Cliente inexistente", "CLIENTE_NO_ENCONTRADO")

        cliente_actualizado = Persona(dni, nombre, apellido)
        asignacion = self._asignar_coche_si_procede(
            cliente_actualizado,
            matricula,
            dni_permitido=dni,
        )
        if not asignacion.ok:
            return asignacion

        return self._concesionario.sustituir_cliente(cliente_actualizado)

    def baja_cliente(self, dni):
        """Da de baja un cliente por DNI."""
        return self._concesionario.eliminar_cliente(dni)

    def transferir_coche(self, dni_vendedor, dni_comprador):
        """Transfiere coche entre clientes localizados por DNI."""
        vendedor = self._concesionario.buscar_cliente_por_dni(dni_vendedor)
        comprador = self._concesionario.buscar_cliente_por_dni(dni_comprador)

        if vendedor is None:
            return Resultado.error("Vendedor no encontrado", "VENDEDOR_NO_ENCONTRADO")
        if comprador is None:
            return Resultado.error("Comprador no encontrado", "COMPRADOR_NO_ENCONTRADO")

        return vendedor.vender_coche(comprador)

    def listar_clientes_con_coche(self):
        """Devuelve una vista simple de clientes para mostrar en la UI."""
        filas = []
        for cliente in self._concesionario.clientes:
            matricula = cliente.coche.matricula if cliente.coche else None
            filas.append(
                {
                    "dni": cliente.dni,
                    "nombre": cliente.nombre,
                    "apellido": cliente.apellido,
                    "matricula": matricula,
                }
            )
        return filas

    def _asignar_coche_si_procede(self, persona, matricula, dni_permitido=None):
        if matricula is None:
            return Resultado.exito("Cliente sin coche")

        coche = self._concesionario.buscar_coche_por_matricula(matricula)
        if coche is None:
            return Resultado.error(
                "No existe un coche con esa matricula en el concesionario",
                "MATRICULA_NO_ENCONTRADA",
            )

        propietario = self._concesionario.buscar_propietario_por_matricula(matricula)
        if propietario is not None and propietario.dni != dni_permitido:
            return Resultado.error(
                (
                    f"La matricula {matricula} ya esta asociada al cliente "
                    f"con DNI {propietario.dni}. Debe transferirse el coche."
                ),
                "MATRICULA_OCUPADA",
            )

        return persona.asignar_coche(coche)

