"""Entidad de persona cliente.

Ejemplo:
    >>> persona = Persona("12345678A", "Ana", "Lopez")
"""

from entities.resultado import Resultado


class Persona:
    """Persona que puede tener como maximo un coche."""

    def __init__(self, dni, nombre, apellido, coche=None):
        self.__dni = str(dni)
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__coche = coche

    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def coche(self):
        return self.__coche

    def asignar_coche(self, coche):
        """Asigna coche si la persona no tiene ya uno."""
        if self.__coche is not None:
            return Resultado.error("La persona ya tiene un coche", "PERSONA_CON_COCHE")
        self.__coche = coche
        return Resultado.exito("Coche asignado")

    def vender_coche(self, a_persona):
        """Transfiere el coche a otra persona si se cumplen validaciones.

        Ejemplo:
            >>> p1 = Persona("1", "A", "B")
            >>> p2 = Persona("2", "C", "D")
            >>> p1.vender_coche(p2).ok
            False
        """
        if self.__coche is None:
            return Resultado.error("La persona vendedora no tiene coche", "VENDEDOR_SIN_COCHE")

        if a_persona.coche is not None:
            return Resultado.error(
                "La persona compradora ya tiene coche",
                "COMPRADOR_CON_COCHE",
            )

        a_persona.__coche = self.__coche
        self.__coche = None
        return Resultado.exito("Transferencia de coche completada")

    def __str__(self):
        coche_txt = self.coche.matricula if self.coche else "sin coche"
        return f"Persona({self.dni}, {self.nombre} {self.apellido}, coche={coche_txt})"

    def __repr__(self):
        return (
            f"Persona({self.dni!r}, {self.nombre!r}, {self.apellido!r}, "
            f"coche={self.coche!r})"
        )

