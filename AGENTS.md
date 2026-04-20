# AGENTS.md — Coches2026

Guía operativa para agentes de IA (Codex, Claude, Gemini CLI, Cursor Agent…) que trabajen en este repositorio.

---

## Qué es este proyecto

Aplicación de consola en **Python 3.12** para gestionar un concesionario de coches.
Proyecto académico: cada sesión añade un concepto OO nuevo sobre la misma base de código.

Arquitectura de cuatro capas con dependencias **estrictamente unidireccionales**:
```
ui  →  services  →  entities  →  (persistence)
```

---

## Comandos esenciales

```bash
# Crear entorno e instalar dependencias
python3 -m venv .venv && source .venv/bin/activate
pip install pytest

# Ejecutar la aplicación
python main.py

# Ejecutar todos los tests
python -m pytest -q

# Ejecutar tests de una capa concreta
python -m pytest tests/test_entities.py -v
```

---

## Estructura del proyecto

```
entities/      # Dominio puro: entidades, invariantes, Resultado
services/      # Casos de uso: orquesta entidades, sin I/O de consola
ui/            # CLI: menús, entrada/salida, llama solo a services
persistence/   # Reservado para adaptadores de almacenamiento
tests/         # Tests por capa: test_entities, test_*_service, test_ui_menu
main.py        # Punto de entrada: construye dependencias y lanza MenuCLI
```

---

## Reglas críticas que nunca debes violar

1. `ui/` **no puede importar** nada de `entities/`. Solo importa de `services/`.
2. `entities/` no contiene `print()`, `input()` ni acceso a ficheros.
3. Toda operación que puede fallar devuelve `Resultado` (nunca lanza excepción al exterior).
4. Atributos de instancia en `entities/` son siempre privados (`self.__nombre`).
5. Type hints obligatorios en todas las firmas públicas.

---

## Dónde encontrar las reglas detalladas

| Qué necesitas saber | Fichero |
|---|---|
| Arquitectura de capas completa | `.github/instructions/architecture.instructions.md` |
| Reglas de dominio y visibilidad OO | `.github/instructions/entities.instructions.md` |
| Convenciones Python del proyecto | `.github/instructions/python-conventions.instructions.md` |
| Cómo escribir tests | `.github/instructions/tests.instructions.md` |
| Reglas de UI | `.github/instructions/ui.instructions.md` |
| Cómo generar diagramas Mermaid | `.github/instructions/mermaid.instructions.md` |

---

## Qué NO hacer

- ❌ No mover ficheros de capa sin actualizar los imports de todas las capas dependientes.
- ❌ No añadir lógica de negocio en `ui/` ni `services/` que pertenezca a `entities/`.
- ❌ No crear tests que instancien entidades en `test_ui_menu.py` (usar mocks de servicios).
- ❌ No subir `.venv/`, `__pycache__/`, `dist/` ni `build/`.

