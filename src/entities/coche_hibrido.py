"""Entidad de coche híbrido con herencia múltiple real.

Ejemplo:
    >>> coche = CocheHibrido("3333CCC", "Toyota")
    >>> coche.recargar(5)
"""

from src.entities.coche_combustion import CocheCombustion
from src.entities.coche_electrico import CocheElectrico
from src.entities.resultado import Resultado


class CocheHibrido(CocheElectrico, CocheCombustion):
    """Coche híbrido que prioriza batería y no mezcla fuentes por avance."""

    def __init__(
        self,
        matricula,
        marca,
        bateria_kwh=0.0,
        gasolina=0.0,
        kilometros_recorridos=0.0,
    ):
        super().__init__(
            matricula=matricula,
            marca=marca,
            bateria_kwh=bateria_kwh,
            gasolina=gasolina,
            kilometros_recorridos=kilometros_recorridos,
        )

    def avanzar(self, km):
        """Avanza usando una sola fuente completa por llamada."""
        km = float(km)
        if km <= 0:
            return Resultado.error("Los kilómetros deben ser mayores que cero", "KM_INVALIDOS")

        if CocheElectrico._energia_suficiente(self, km):
            CocheElectrico._consumir_energia(self, km)
            self._registrar_avance(km)
            return Resultado.exito("Avance completado en modo electrico", valor="electrico")

        if CocheCombustion._energia_suficiente(self, km):
            CocheCombustion._consumir_energia(self, km)
            self._registrar_avance(km)
            return Resultado.exito("Avance completado en modo combustion", valor="combustion")

        return Resultado.error(
            "Ni bateria ni gasolina cubren por si solas el recorrido",
            "ENERGIA_INSUFICIENTE",
        )

    def __repr__(self):
        return (
            f"CocheHibrido({self.matricula!r}, {self.marca!r}, bateria_kwh={self.bateria_kwh!r}, "
            f"gasolina={self.gasolina!r}, kilometros_recorridos={self.kilometros_recorridos!r})"
        )

