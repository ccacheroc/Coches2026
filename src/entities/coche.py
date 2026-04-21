"""Clase base abstracta para coches.

Ejemplo:
    Usar subclases como CocheCombustion o CocheElectrico.
"""

from abc import ABC, abstractmethod

from src.entities.resultado import Resultado


class Coche(ABC):
    """Comportamiento común de cualquier coche."""

    _kilometros_por_marca = {}

    def __init__(self, matricula, marca, kilometros_recorridos=0.0, **_kwargs):
        self.__matricula = str(matricula)
        self.__marca = str(marca)
        self.__kilometros_recorridos = float(kilometros_recorridos)
        self._sumar_kilometros_marca(self.__marca, self.__kilometros_recorridos)

    @property
    def matricula(self):
        return self.__matricula

    @property
    def marca(self):
        return self.__marca

    @property
    def kilometros_recorridos(self):
        return self.__kilometros_recorridos

    @classmethod
    def obtener_kilometros_por_marca(cls, marca):
        """Devuelve kilómetros acumulados para una marca.

        Ejemplo:
            >>> Coche.obtener_kilometros_por_marca("Tesla")
            0.0
        """
        return float(cls._kilometros_por_marca.get(str(marca), 0.0))

    @classmethod
    def listar_kilometros_por_marca(cls):
        """Devuelve todos los acumulados de kilómetros por marca."""
        return {marca: float(km) for marca, km in cls._kilometros_por_marca.items()}

    @classmethod
    def _sumar_kilometros_marca(cls, marca, km):
        cls._kilometros_por_marca[marca] = cls.obtener_kilometros_por_marca(marca) + float(km)

    def _registrar_avance(self, km):
        self.__kilometros_recorridos += float(km)
        self._sumar_kilometros_marca(self.__marca, km)

    @abstractmethod
    def _energia_suficiente(self, km):
        pass

    @abstractmethod
    def _consumir_energia(self, km):
        pass

    @abstractmethod
    def _tipo_energia(self):
        pass

    def avanzar(self, km):
        """Intenta avanzar kilómetros usando la energía de la subclase."""
        km = float(km)
        if km <= 0:
            return Resultado.error("Los kilómetros deben ser mayores que cero", "KM_INVALIDOS")

        if not self._energia_suficiente(km):
            return Resultado.error(
                f"Energía insuficiente para avanzar {km} km en modo {self._tipo_energia()}",
                "ENERGIA_INSUFICIENTE",
            )

        self._consumir_energia(km)
        self._registrar_avance(km)
        return Resultado.exito(f"Se avanzaron {km} km", valor=km)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(matricula={self.matricula}, marca={self.marca}, "
            f"km={self.kilometros_recorridos:.2f})"
        )

