---
applyTo: 'persistence/**/*.py'
description: 'Reglas específicas para la capa de persistencia (persistence/)'
---

# Reglas — Capa `persistence/`

## Responsabilidad

Esta capa implementa **adaptadores de almacenamiento**: serializa entidades a disco y las deserializa al arrancar.
Es la única capa que hace I/O de ficheros.

## Dependencias permitidas

- ✅ Importar desde `entities/` (solo para reconstruir objetos con `from_dict` / `pickle.load`).
- ❌ Importar desde `ui/` o `services/`.
- ❌ Lógica de negocio aquí — solo serialización / deserialización.

## Interfaz esperada de cada adaptador

Cada repositorio debe implementar al menos estos dos métodos:

```python
def guardar(self, datos: list) -> None:
    """Persiste la lista de objetos en el soporte elegido."""
    ...

def cargar(self) -> list:
    """Carga y devuelve la lista de objetos. Devuelve [] si no existe el fichero."""
    ...
```

## Adaptadores de texto (JSON)

```python
import json
from pathlib import Path

class CochesRepoJson:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def guardar(self, coches: list) -> None:
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in coches], f, ensure_ascii=False, indent=2)

    def cargar(self) -> list:
        try:
            with open(self.__path, encoding="utf-8") as f:
                return [CocheCombustion.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            return []
```

## Adaptadores binarios (Pickle)

```python
import pickle
from pathlib import Path

# WARNING: nunca cargar ficheros pickle de fuentes no confiables (riesgo de ejecución arbitraria).
class CochesRepoBin:
    def guardar(self, coches: list) -> None:
        with open(self.__path, "wb") as f:
            pickle.dump(coches, f)

    def cargar(self) -> list:
        try:
            with open(self.__path, "rb") as f:
                return pickle.load(f)  # noqa: S301
        except FileNotFoundError:
            return []
```

## Paths

Usar siempre `pathlib.Path`. El path se **inyecta** en el constructor; nunca se hardcodea dentro del adaptador.

## Cuándo añadir un adaptador nuevo

1. Crear el fichero en `persistence/` con nombre `<entidad>_repo_<formato>.py`.
2. Inyectarlo en `services/` desde `main.py`.
3. Añadir test con `tmp_path` de pytest (sin tocar ficheros reales).

