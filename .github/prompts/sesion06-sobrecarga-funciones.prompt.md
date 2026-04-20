---
mode: 'agent'
description: 'Sesión 6 — Implementar sobrecarga de funciones built-in (__str__, __repr__, __len__, __bool__)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 6** de la asignatura.
El objetivo de hoy es implementar la **sobrecarga de funciones built-in** de Python.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Implementar `__str__` en todas las entidades para producir salida legible por el usuario final.
2. Implementar `__repr__` con información técnica para depuración.
3. Identificar dónde tiene sentido `__len__` (ej. en clases que contienen colecciones de elementos).
4. Implementar `__bool__` donde aplique (ej. `Resultado`: `True` si `ok`, entidad: `True` si tiene recursos disponibles).
5. Verificar que `ui/` usa `str(objeto)` en lugar de acceder a atributos directamente.
6. Añadir tests para cada dunder implementado.

# REGLAS ESTRICTAS PARA HOY

- `__str__` va en `entities/`; la UI solo llama a `str(objeto)`.
- `__repr__` debe permitir identificar el objeto unívocamente (clase + atributos clave).
- No implementar `__eq__` ni `__hash__` hoy (es Sesión 7).

# MODO TUTOR

Muestra el `__str__` de la clase principal como ejemplo. Pide al alumno que implemente `__repr__` y `__bool__` antes de revelar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion06: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `__str__` implementado en todas las entidades — la salida es legible para el usuario
- [ ] `__repr__` implementado en todas las entidades — incluye clase y atributos clave
- [ ] `__bool__` implementado donde aplique con semántica clara
- [ ] `ui/` usa `str(objeto)` y no accede a propiedades internas para mostrar datos: `grep -rn "\.__" ui/`
- [ ] Tests de `__str__`, `__repr__` y `__bool__` pasan

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion06.md` y haz commit:

```markdown
# Journal — Sesión 06 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Dunders implementados por clase
<!-- Lista: clase → __str__ / __repr__ / __len__ / __bool__ -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: __bool__ de Resultado devuelve self.ok porque es la semántica más natural -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion06.md
git commit -m "sesion06: journal de sesión"
git push origin main
```
