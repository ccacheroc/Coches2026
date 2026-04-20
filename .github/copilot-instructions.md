# Instrucciones globales para GitHub Copilot — Coches2026

Este fichero se aplica a **todo** el repositorio en todo momento.
Referencia las instrucciones específicas en `instructions/` y los workflows en `workflows/`.

---

## Contexto del proyecto

Aplicación de consola en Python 3.12 para gestionar un concesionario.
Dominio académico: las sesiones de la asignatura añaden gradualmente conceptos OO.
Arquitectura de **cuatro capas** con dependencias unidireccionales:

```
ui  →  services  →  entities  →  (persistence)
```

Consulta `instructions/architecture.instructions.md` para las reglas completas.

---

## Reglas que NUNCA deben violarse

1. **`ui` no puede importar `entities`** — solo puede importar `services`.
2. **`entities` no tiene I/O** — ningún `print()`, `input()` ni acceso a ficheros en esta capa.
3. **`services` no tiene I/O de consola** — solo orquesta entidades.
4. **Toda operación que puede fallar devuelve `Resultado`** (`entities/resultado.py`).
5. **Atributos de dominio son privados** (`__nombre`) y se exponen solo con `@property` de lectura si es necesario. Añadir setter solo si hay lógica de validación o la mutación es parte del dominio. Ver `instructions/oo-design.instructions.md`.
6. **Python 3.12+**, type hints en todas las firmas públicas.
7. **Tests con pytest**; usar `Given/When/Then` en comentarios. Mocks solo en la capa de servicios, nunca en entidades.

---

## Cómo usar los ficheros de contexto

| Fichero | Cuándo cargarlo |
|---|---|
| `instructions/architecture.instructions.md` | Siempre que se añada o mueva código entre capas |
| `instructions/python-conventions.instructions.md` | Siempre que se genere código Python |
| `instructions/oo-design.instructions.md` | Al diseñar o revisar clases y atributos |
| `skills/mermaid-class-diagram.md` | Al generar o actualizar el diagrama UML de clases |
| `skills/mermaid-c4-diagram.md` | Al generar o actualizar el diagrama C4 |
| `skills/tdd-pytest.md` | Al escribir o revisar tests |
| `workflows/sesionXX-*.md` | Al iniciar o continuar la sesión activa |

