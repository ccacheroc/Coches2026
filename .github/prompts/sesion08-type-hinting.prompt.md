---
mode: 'agent'
description: 'Sesión 8 — Añadir type hinting completo (PEP 484 / PEP 526)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 8** de la asignatura.
El objetivo de hoy es añadir **type hinting completo** (PEP 484 / PEP 526) a todo el código.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Añadir type hints a **todas** las firmas públicas que aún no los tengan:
   - Parámetros y tipo de retorno en métodos y funciones.
   - Atributos de instancia en `__init__`.
2. Usar tipos modernos (Python 3.10+):
   - `list[MiEntidad]` en lugar de `list` sin anotar.
   - `MiEntidad | None` para opcionales (nunca `Optional[X]`).
   - `ClassVar[dict[str, float]]` para atributos de clase.
3. Verificar con `mypy` o `pyright`:
   ```bash
   pip install mypy
   mypy entities/ services/ ui/ --strict
   ```
4. Corregir los errores encontrados sin cambiar la lógica de negocio.
5. Actualizar tests si alguna firma ha cambiado.

# REGLAS ESTRICTAS PARA HOY

- No usar `Any` salvo en `Resultado.valor` (deliberado y documentado).
- No usar `Optional[X]`; usar `X | None`.
- No alterar la lógica de negocio; hoy solo se añaden anotaciones.

# MODO TUTOR

Muestra cómo anotar `__init__` y un atributo de clase de la entidad principal. Luego pide al alumno que anote las demás clases.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion08: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `mypy entities/ services/ ui/ --strict` → 0 errores
- [ ] Ningún `Optional[X]` en el código — solo `X | None`: `grep -rn "Optional" entities/ services/ ui/` → vacío
- [ ] Ningún `Any` sin comentario que justifique su uso
- [ ] Todos los `__init__` tienen atributos anotados (`self.__x: tipo = valor`)
- [ ] Los atributos de clase tienen `ClassVar[...]`

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion08.md` y haz commit:

```markdown
# Journal — Sesión 08 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Errores de mypy encontrados y cómo los resolvimos


## Decisiones de tipado tomadas (y por qué)
<!-- Ej: usamos Any en Resultado.valor porque puede ser de cualquier tipo -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion08.md
git commit -m "sesion08: journal de sesión"
git push origin main
```
