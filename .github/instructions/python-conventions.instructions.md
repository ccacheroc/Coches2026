---
applyTo: '**/*.py'
description: 'Convenciones Python para el proyecto Coches2026'
---

# Convenciones Python — Coches2026

## Versión y herramientas

- **Python 3.12+** obligatorio.
- Formateo: `black` (líneas ≤ 88 caracteres).
- Linting: `ruff`.
- Tests: `pytest`.

## Type hints

Todas las firmas públicas llevan type hints. Sin excepciones.

```python
# ✅ Correcto
def repostar(self, litros: float) -> Resultado:
    ...

# ❌ Incorrecto
def repostar(self, litros):
    ...
```

Usar `|` en lugar de `Optional` para tipos nullables (Python 3.10+):

```python
def __init__(self, coche: Coche | None = None) -> None:
```

## Nomenclatura

| Elemento | Convención | Ejemplo |
|---|---|---|
| Clases | `PascalCase` | `CocheCombustion` |
| Métodos / funciones | `snake_case` | `avanzar_km` |
| Atributos privados | `__doble_guion` | `self.__matricula` |
| Atributos protegidos | `_un_guion` (solo si herencia lo requiere) | `self._energia` |
| Constantes de módulo | `UPPER_SNAKE` | `CONSUMO_GASOLINA` |

## Docstrings

Docstring corto en todas las clases y métodos públicos. Formato:

```python
def avanzar(self, km: float) -> Resultado:
    """Avanza el coche la distancia indicada consumiendo energía.

    Args:
        km: Kilómetros a recorrer (debe ser > 0).

    Returns:
        Resultado con ok=True si el avance fue posible.

    Example:
        >>> c = CocheCombustion("1234ABC", "Seat")
        >>> c.repostar(10)
        >>> c.avanzar(50).ok
        True
    """
```

## Errores y excepciones

- En `entities/` y `services/`: **nunca** lanzar excepciones al llamador; devolver `Resultado.error(...)`.
- Solo lanzar excepciones internas (`ValueError`, `TypeError`) para programación defensiva dentro del método, si la situación es un bug (no un flujo de negocio esperado).

## `__str__` y `__repr__`

- `__str__`: legible para el usuario final (usado en `ui/`).
- `__repr__`: información técnica útil para depuración.

```python
def __str__(self) -> str:
    return f"{self.__marca} ({self.__matricula}) — {self.__kilometros_recorridos:.1f} km"

def __repr__(self) -> str:
    return f"CocheCombustion(matricula={self.__matricula!r}, marca={self.__marca!r})"
```

## Imports

Orden: stdlib → third-party → proyecto (separados por línea en blanco).
No usar imports relativos (`from . import`) salvo en `__init__.py`.

