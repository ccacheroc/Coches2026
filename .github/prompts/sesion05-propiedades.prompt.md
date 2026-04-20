---
mode: 'agent'
description: 'Sesión 5 — Añadir @property, herencia múltiple y clases abstractas'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 5** de la asignatura.
El objetivo de hoy es enriquecer el diseño con **propiedades (`@property`)**, **herencia múltiple** y **clases abstractas** donde proceda.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Convertir la clase base principal en clase abstracta con `ABC` y decorar con `@abstractmethod` los métodos que cada subclase debe implementar obligatoriamente.
2. Identificar qué atributos necesitan `@property` de lectura (los que `services/` o `ui/` necesitan leer). Ver `instructions/entities.instructions.md`.
3. Añadir setter `@atributo.setter` solo donde la mutación tenga lógica de validación.
4. Si el dominio lo requiere, implementar herencia múltiple documentando el MRO elegido con un comentario.
5. Actualizar el diagrama de clases en `README.md`.
6. Verificar que todos los tests existentes siguen pasando.

# REGLAS ESTRICTAS PARA HOY

- La clase base abstracta no puede instanciarse directamente; debe lanzar `TypeError` si se intenta.
- No añadir setter si no hay validación real. Ver `instructions/entities.instructions.md`.
- El orden MRO en herencia múltiple debe ser explícito y documentado con un comentario en la clase.

# MODO TUTOR

Muestra cómo declarar la clase base como abstracta. Luego pide al alumno que identifique qué `@property` son necesarias antes de implementarlas.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion05: descripción corta`

## Quality gates específicos de esta sesión
- [ ] La clase base tiene `ABC` e `@abstractmethod` — `pytest.raises(TypeError)` al instanciarla directamente
- [ ] Todas las propiedades observables tienen `@property` de lectura sin setter (salvo validación justificada)
- [ ] Ningún setter añadido sin lógica de validación real
- [ ] Si hay herencia múltiple, el MRO está documentado con comentario en la clase
- [ ] `services/` sigue sin importar `entities/` directamente en tests de UI
- [ ] Diagrama de clases actualizado con `<<abstract>>` y propiedades `+`

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion05.md` y haz commit:

```markdown
# Journal — Sesión 05 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Properties añadidas y justificación
<!-- Lista: atributo → @property de lectura / setter / ninguna — y por qué -->

## Decisiones sobre herencia múltiple o clases abstractas
<!-- ¿Había candidatos? ¿Qué decidisteis y por qué? -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion05.md
git commit -m "sesion05: journal de sesión"
git push origin main
```
