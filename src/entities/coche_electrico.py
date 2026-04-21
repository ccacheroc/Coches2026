"""Entidad de coche eléctrico.

Ejemplo:
    >>> coche = CocheElectrico("2222BBB", "Tesla")
    >>> coche.recargar(20)
"""

from src.entities.coche import Coche
from src.entities.resultado import Resultado


class CocheElectrico(Coche):
    """Coche que consume batería."""

    CONSUMO_KWH_POR_KM = 0.02

    def __init__(
        self,
        matricula,
        marca,
        bateria_kwh=0.0,
        kilometros_recorridos=0.0,
        **kwargs,
    ):
        super().__init__(
            matricula=matricula,
            marca=marca,
            kilometros_recorridos=kilometros_recorridos,
            **kwargs,
        )
        self.__bateria_kwh = float(bateria_kwh)

    @property
    def bateria_kwh(self):
        return self.__bateria_kwh

    def recargar(self, kwh):
        """Añade energía a la batería si el valor es válido.

        Ejemplo:
            >>> CocheElectrico("1", "Tesla").recargar(3).ok
            True
        """
        kwh = float(kwh)
        if kwh <= 0:
            return Resultado.error("Los kWh deben ser mayores que cero", "KWH_INVALIDOS")

        self.__bateria_kwh += kwh
        return Resultado.exito(f"Recargados {kwh} kWh", valor=self.__bateria_kwh)

    def _energia_suficiente(self, km):
        return self.__bateria_kwh >= km * self.CONSUMO_KWH_POR_KM

    def _consumir_energia(self, km):
        self.__bateria_kwh -= km * self.CONSUMO_KWH_POR_KM

    def _tipo_energia(self):
        return "eléctrico"

    def __repr__(self):
        return (
            f"CocheElectrico({self.matricula!r}, {self.marca!r}, bateria_kwh={self.bateria_kwh!r}, "
            f"kilometros_recorridos={self.kilometros_recorridos!r})"
        )

