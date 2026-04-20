# Instrucciones globales para GitHub Copilot — Coches2026

Aplicación de consola en Python 3.12 para gestionar un concesionario.
Dominio académico: las sesiones de la asignatura añaden gradualmente conceptos OO.
Arquitectura de **cuatro capas** con dependencias unidireccionales:

```
ui  →  services  →  entities  →  (persistence)
```

---

## Reglas que NUNCA deben violarse

1. **`ui` no puede importar `entities`** — solo puede importar `services`.
2. **`entities` no tiene I/O** — ningún `print()`, `input()` ni acceso a ficheros.
3. **`services` no tiene I/O de consola** — solo orquesta entidades.
4. **Toda operación que puede fallar devuelve `Resultado`** (`entities/resultado.py`).
5. **Atributos de dominio son privados** (`__nombre`); expuestos solo con `@property` de lectura. Setter solo si hay validación de dominio.
6. **Python 3.12+**, type hints en todas las firmas públicas.
7. **Tests con pytest**; estructura `Given/When/Then`. Mocks solo en tests de servicios y UI, nunca en tests de entidades.

---

## Mapa de ficheros de contexto

| Fichero | Se activa | Contenido |
|---|---|---|
| `instructions/architecture.instructions.md` | `**/*.py` (auto) | Capas, dependencias, checklist de nueva funcionalidad |
| `instructions/python-conventions.instructions.md` | `**/*.py` (auto) | Type hints, nomenclatura, docstrings, imports |
| `instructions/entities.instructions.md` | `entities/**/*.py` (auto) | Reglas de dominio, visibilidad, `@property`, setters |
| `instructions/services.instructions.md` | `services/**/*.py` (auto) | Casos de uso, gestión de errores, seed |
| `instructions/ui.instructions.md` | `ui/**/*.py` (auto) | Prohibición de importar entities, patrón de llamada a servicios |
| `instructions/persistence.instructions.md` | `persistence/**/*.py` (auto) | Adaptadores JSON/Pickle, interfaz de repositorio |
| `instructions/tests.instructions.md` | `tests/**/*.py` (auto) | Given/When/Then, mocks en UI, nombrado de tests |
| `instructions/mermaid.instructions.md` | `README.md` (auto) | Reglas UML classDiagram y C4Container |
| `prompts/sesionXX-*.prompt.md` | manual con `/nombre` | Contexto pedagógico y tareas por sesión |
