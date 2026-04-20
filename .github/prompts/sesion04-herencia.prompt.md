---
mode: 'agent'
description: 'Sesión 4 — Refinar el diagrama y el código añadiendo relaciones de herencia'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 4** de la asignatura.
El objetivo de hoy es refinar nuestro diagrama de clases y el código de la capa de `entities/` añadiendo relaciones de herencia.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)
1. Analizar las entidades actuales y detectar oportunidades de herencia (clases padre e hijas).
2. Crear la clase padre con los atributos comunes.
3. Refactorizar las clases hijas usando `super().__init__()`.
4. Asegurarse de que estos cambios no rompen la capa de `services/`.
5. Actualizar el diagrama de clases en `README.md`.
6. Añadir o actualizar tests para verificar que la herencia funciona correctamente.

# REGLAS ESTRICTAS PARA HOY

- No uses propiedades ni clases abstractas todavía (eso es para la Sesión 5).
- Actúa como un tutor: no des el código de todas las clases hijas de golpe. Haz un ejemplo con una y pide al alumno que haga el resto.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion04: descripción corta`

## Quality gates específicos de esta sesión
- [ ] Existe al menos una relación de herencia en `entities/`
- [ ] Las clases hijas llaman a `super().__init__()` con los parámetros correctos
- [ ] No se repiten atributos en las clases hijas que ya están en la clase padre
- [ ] `isinstance(hijo, Padre)` devuelve `True`
- [ ] Tests que verifican el comportamiento heredado pasan
- [ ] Diagrama de clases actualizado en `README.md` con flechas `<|--`

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion04.md` y haz commit:

```markdown
# Journal — Sesión 04 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Jerarquía de herencia implementada
<!-- Ej: ClasePadre → ClaseHijaA, ClaseHijaB -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: pusimos X en la clase padre porque todas las hijas lo necesitan -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion04.md
git commit -m "sesion04: journal de sesión"
git push origin main
```
