"""Servicio para cargar datos de ejemplo al arrancar.

Ejemplo:
    >>> # SeedDataService(...).cargar_datos_demo()
"""

from entities.resultado import Resultado


class SeedDataService:
    """Inserta datos de demostracion en memoria usando casos de uso existentes."""

    def __init__(self, concesionario_service, personas_service):
        self._concesionario_service = concesionario_service
        self._personas_service = personas_service

    def cargar_datos_demo(self):
        """Carga datos iniciales solo si el concesionario esta vacio."""
        resumen = self._concesionario_service.resumen()
        if resumen["num_coches"] > 0 or resumen["num_clientes"] > 0:
            return Resultado.exito("Seed omitido: ya existen datos en memoria")

        coches_demo = [
            ("combustion", "1234ABC", "Seat"),
            ("electrico", "2345BCD", "Tesla"),
            ("hibrido", "3456CDE", "Toyota"),
            ("combustion", "4567DEF", "Ford"),
            ("electrico", "5678EFG", "Kia"),
        ]
        for tipo, matricula, marca in coches_demo:
            resultado = self._concesionario_service.alta_coche(tipo, matricula, marca)
            if not resultado.ok:
                return resultado

        clientes_demo = [
            ("11111111A", "Ana", "Lopez", "1234ABC"),
            ("22222222B", "Luis", "Perez", "2345BCD"),
            ("33333333C", "Marta", "Sanchez", None),
            ("44444444D", "Carlos", "Ruiz", "3456CDE"),
        ]
        for dni, nombre, apellido, matricula in clientes_demo:
            resultado = self._personas_service.alta_cliente(
                dni,
                nombre,
                apellido,
                matricula=matricula,
            )
            if not resultado.ok:
                return resultado

        return Resultado.exito(
            "Seed cargado correctamente",
            valor={"coches": len(coches_demo), "clientes": len(clientes_demo)},
        )

