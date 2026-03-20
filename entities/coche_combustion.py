"""Entidad de coche de combustión.

Ejemplo:
    >>> coche = CocheCombustion("1111AAA", "Ford")
    >>> coche.repostar(10)
"""

from entities.coche import Coche
from entities.resultado import Resultado


class CocheCombustion(Coche):
    """Coche que consume gasolina."""

    CONSUMO_LITROS_POR_KM = 0.05

    def __init__(
        self,
        matricula,
        marca,
        gasolina=0.0,
        kilometros_recorridos=0.0,
        **kwargs,
    ):
        super().__init__(
            matricula=matricula,
            marca=marca,
            kilometros_recorridos=kilometros_recorridos,
            **kwargs,
        )
        self.__gasolina = float(gasolina)

    @property
    def gasolina(self):
        return self.__gasolina

    def repostar(self, litros):
        """Añade gasolina si el valor es válido.

        Ejemplo:
            >>> CocheCombustion("1", "Seat").repostar(5).ok
            True
        """
        litros = float(litros)
        if litros <= 0:
            return Resultado.error("Los litros deben ser mayores que cero", "LITROS_INVALIDOS")

        self.__gasolina += litros
        return Resultado.exito(f"Repostados {litros} litros", valor=self.__gasolina)

    def _energia_suficiente(self, km):
        return self.__gasolina >= km * self.CONSUMO_LITROS_POR_KM

    def _consumir_energia(self, km):
        self.__gasolina -= km * self.CONSUMO_LITROS_POR_KM

    def _tipo_energia(self):
        return "gasolina"

    def __repr__(self):
        return (
            f"CocheCombustion({self.matricula!r}, {self.marca!r}, gasolina={self.gasolina!r}, "
            f"kilometros_recorridos={self.kilometros_recorridos!r})"
        )

