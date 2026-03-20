"""Contrato de resultados para operaciones del dominio.

Ejemplo:
    >>> Resultado.exito("Cliente anadido").ok
    True
"""


class Resultado:
    """Representa el resultado uniforme de una operación."""

    def __init__(self, ok, mensaje, codigo=None, valor=None):
        self.ok = bool(ok)
        self.mensaje = str(mensaje)
        self.codigo = codigo
        self.valor = valor

    @classmethod
    def exito(cls, mensaje="Operación completada", valor=None):
        """Crea un resultado exitoso.

        Ejemplo:
            >>> Resultado.exito("Hecho").ok
            True
        """
        return cls(True, mensaje, codigo=None, valor=valor)

    @classmethod
    def error(cls, mensaje, codigo="ERROR", valor=None):
        """Crea un resultado de error.

        Ejemplo:
            >>> Resultado.error("Sin batería", "ENERGIA").ok
            False
        """
        return cls(False, mensaje, codigo=codigo, valor=valor)

    def __bool__(self):
        return self.ok

    def __repr__(self):
        return (
            f"Resultado(ok={self.ok!r}, mensaje={self.mensaje!r}, "
            f"codigo={self.codigo!r}, valor={self.valor!r})"
        )

