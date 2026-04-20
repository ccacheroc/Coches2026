---
applyTo: 'entities/**/*.py'
description: 'Reglas específicas para la capa de dominio (entities/)'
---

# Reglas — Capa `entities/`

## Responsabilidad

Esta capa contiene el **modelo de dominio puro**: entidades, invariantes y reglas de negocio.
No tiene dependencias con ninguna otra capa del proyecto.

## Prohibiciones absolutas

- ❌ `print()`, `input()` o cualquier I/O de consola.
- ❌ Acceso a ficheros, red o base de datos.
- ❌ Importar desde `services/`, `ui/` o `persistence/`.
- ❌ Atributos de instancia públicos sin pasar por `@property`.

## Atributos — Visibilidad obligatoria

Todos los atributos de instancia son **privados** (`self.__nombre`).
Se exponen solo con `@property` de lectura si otra capa los necesita.
Añadir setter únicamente si la mutación tiene lógica de validación.
Ver criterio completo en `instructions/oo-design.instructions.md`.

```python
class Coche(ABC):
    def __init__(self, matricula: str, marca: str) -> None:
        if not matricula:
            raise ValueError("La matrícula no puede estar vacía")
        self.__matricula: str = matricula
        self.__marca: str = marca
        self.__kilometros_recorridos: float = 0.0

    @property
    def matricula(self) -> str:
        return self.__matricula
```

## Contrato de errores

Toda operación que puede fallar por **lógica de negocio** devuelve `Resultado`:

```python
def avanzar(self, km: float) -> Resultado:
    if km <= 0:
        return Resultado.error("Los km deben ser positivos", "KM_INVALIDOS")
    ...
    return Resultado.exito(f"Avanzado {km} km")
```

Las excepciones (`ValueError`, clases propias de `excepciones.py`) se reservan para **invariantes de construcción** (datos de entrada inválidos que son un bug del llamador).

## Atributos de clase

Usar `ClassVar` y documentar su propósito:

```python
from typing import ClassVar

class Coche(ABC):
    __km_por_marca: ClassVar[dict[str, float]] = {}
```

## Type hints

Obligatorios en todas las firmas públicas. Usar `X | None` (nunca `Optional[X]`).

## Clases abstractas

`Coche` es abstracta (`ABC`). Decorar con `@abstractmethod` los métodos que cada subclase debe implementar obligatoriamente (`avanzar`).

## Herencia múltiple

`CocheHibrido` hereda de `CocheElectrico` y `CocheCombustion`.
Documentar el MRO elegido con un comentario en la clase:

```python
# MRO: CocheHibrido → CocheElectrico → CocheCombustion → Coche
class CocheHibrido(CocheElectrico, CocheCombustion):
    ...
```

