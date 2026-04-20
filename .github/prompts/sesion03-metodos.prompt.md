---
mode: 'agent'
description: 'Sesión 3 — Añadir métodos de instancia y de clase a las entidades'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 3** de la asignatura.
El objetivo de hoy es enriquecer el diagrama de clases y el código con **métodos de instancia y de clase**.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Revisar el diagrama de clases actual e identificar qué comportamientos faltan.
2. Añadir **métodos de instancia** a cada entidad que implementen las operaciones del dominio.
3. Añadir **métodos de clase** donde aplique (operaciones sobre el estado compartido de la clase).
4. Todas las operaciones que pueden fallar devuelven `Resultado`. Ver `instructions/architecture.instructions.md`.
5. Actualizar el diagrama Mermaid en `README.md`.
6. Escribir/ampliar tests con Given/When/Then para cada método nuevo.

# REGLAS ESTRICTAS PARA HOY

- Ningún método en `entities/` puede contener `print()` ni `input()`.
- Los métodos de clase se decoran con `@classmethod` y reciben `cls` como primer parámetro.
- No añadir herencia todavía (es Sesión 4).
- `Resultado` es obligatorio para toda operación que pueda fallar.

# MODO TUTOR

Muestra un método de instancia de la clase principal como ejemplo. Luego pide al alumno que implemente los métodos de las demás clases antes de mostrar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion03: descripción corta`

## Quality gates específicos de esta sesión
- [ ] Cada entidad tiene al menos un método de instancia que implementa una operación del dominio
- [ ] Toda operación que puede fallar devuelve `Resultado` (ninguna lanza excepción al exterior)
- [ ] Ningún método en `entities/` contiene `print()` ni `input()`: `grep -rn "print\|input" entities/`
- [ ] Métodos de clase decorados con `@classmethod` donde aplique
- [ ] Tests Given/When/Then escritos para cada método nuevo (happy path + error de dominio)
- [ ] Diagrama de clases actualizado en `README.md` con los métodos nuevos

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion03.md` y haz commit:

```markdown
# Journal — Sesión 03 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Métodos implementados por clase
<!-- Lista los métodos añadidos a cada clase y su propósito -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: decidimos que X devuelve Resultado en lugar de lanzar excepción porque... -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion03.md
git commit -m "sesion03: journal de sesión"
git push origin main
```
