---
mode: 'agent'
description: 'Sesión 9 — Añadir jerarquía de excepciones propias del dominio'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 9** de la asignatura.
El objetivo de hoy es añadir **manejo de excepciones** propio del dominio.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Crear una jerarquía de excepciones propias en `entities/excepciones.py`:
   ```python
   class AppError(Exception): ...           # base de todas las excepciones del proyecto
   class IdentificadorInvalidoError(AppError): ...
   class RecursoInsuficienteError(AppError): ...
   class ElementoDuplicadoError(AppError): ...
   # Añadir las que el dominio del proyecto necesite
   ```
2. Lanzar estas excepciones en `__init__` para **invariantes de construcción** (datos de entrada inválidos).
3. **Mantener `Resultado`** para errores de flujo de negocio esperados (operación que falla por lógica, no por bug).
4. Capturar excepciones en `ui/` y mostrar mensaje amigable al usuario.
5. Añadir tests que verifiquen que las excepciones se lanzan en los casos correctos.

# CRITERIO: excepción vs Resultado

| Situación | Mecanismo |
|---|---|
| Identificador vacío al construir la entidad | `raise IdentificadorInvalidoError` |
| Operación que falla por falta de recursos | `return Resultado.error(...)` |
| Formato de dato inválido en construcción | `raise ValueError` o excepción propia |
| Elemento ya registrado en la colección | `return Resultado.error(...)` |

# REGLAS ESTRICTAS PARA HOY

- Las excepciones del dominio heredan de `AppError`, no directamente de `Exception`.
- `services/` no lanza excepciones propias; las deja propagar o las convierte en `Resultado`.
- `ui/` captura excepciones y las muestra como mensajes de error sin stack trace.

# MODO TUTOR

Muestra cómo crear `AppError` y la primera excepción específica. Pide al alumno que añada la validación en `__init__` de la entidad principal antes de mostrar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion09: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `entities/excepciones.py` existe con jerarquía propia (`AppError` como base)
- [ ] Las excepciones propias heredan de `AppError`, no directamente de `Exception`
- [ ] Tests que verifican `pytest.raises(ExcepcionPropia)` al construir con datos inválidos
- [ ] `ui/` captura excepciones y muestra mensaje sin stack trace (no `traceback` visible al usuario)
- [ ] El criterio excepción vs `Resultado` es coherente y consistente en todo el código

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion09.md` y haz commit:

```markdown
# Journal — Sesión 09 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Jerarquía de excepciones creada
<!-- Lista las excepciones y cuándo se lanzan -->

## Casos que usan excepción vs Resultado
<!-- Documenta los casos límite y la decisión tomada -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion09.md
git commit -m "sesion09: journal de sesión"
git push origin main
```
