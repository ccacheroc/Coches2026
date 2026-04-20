---
mode: 'agent'
description: 'Sesión 2 — Definir el diagrama de clases inicial y crear los esqueletos de clase en entities/'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 2** de la asignatura.
El objetivo de hoy es diseñar el diagrama de clases inicial de nuestra app y crear los esqueletos de clase en `entities/`.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. A partir de la idea del proyecto, identificar las **clases principales** del dominio.
2. Definir los **atributos de instancia** de cada clase (con tipo y visibilidad).
3. Definir si hay **atributos de clase** (compartidos por todas las instancias).
4. Generar el diagrama de clases en Mermaid (usar `/mermaid-class-diagram` o ver `instructions/mermaid.instructions.md`).
5. Implementar los esqueletos de clase en `entities/`:
   - Solo `__init__` con atributos privados.
   - Sin métodos de negocio todavía (eso es Sesión 3).
   - Sin herencia todavía (eso es Sesión 4).
6. Añadir `__str__` básico para poder imprimir objetos en la consola.
7. Crear tests mínimos que comprueben que los objetos se crean correctamente.

# REGLAS ESTRICTAS PARA HOY

- Todos los atributos de dominio son privados (`self.__nombre`). Ver `instructions/entities.instructions.md`.
- No implementar lógica de negocio todavía; solo la estructura.
- No añadir `@property` todavía salvo que sean imprescindibles para los tests.
- El fichero `entities/resultado.py` debe existir con `Resultado.exito` y `Resultado.error`.

# MODO TUTOR

Propón la primera clase principal con sus atributos. Luego pide al alumno que implemente las demás antes de mostrar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

Antes de cerrar la sesión, verifica que se cumplen **todos** los criterios:

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion02: descripción corta`

## Quality gates específicos de esta sesión
- [ ] Al menos 3 clases de dominio creadas en `entities/`
- [ ] Todos los atributos de instancia son `self.__privado` (doble guion)
- [ ] `entities/resultado.py` existe con `Resultado.exito` y `Resultado.error`
- [ ] `__str__` implementado en todas las clases nuevas
- [ ] Tests de construcción pasan (objetos se crean correctamente)
- [ ] Diagrama de clases actualizado en `README.md`

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion02.md` y haz commit:

```markdown
# Journal — Sesión 02 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Clases identificadas y atributos principales
<!-- Lista las clases creadas y sus atributos más relevantes -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: decidimos que X es privado porque modificarlo directamente rompería... -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion02.md
git commit -m "sesion02: journal de sesión"
git push origin main
```
