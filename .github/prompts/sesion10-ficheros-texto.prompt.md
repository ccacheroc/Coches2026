---
mode: 'agent'
description: 'Sesión 10 — Añadir persistencia en ficheros de texto plano (JSON/CSV)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 10** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros de texto plano**.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Decidir el formato de serialización (recomendado: JSON por legibilidad). Documentar la decisión.
2. Crear adaptadores en `persistence/`:
   - Un adaptador por cada entidad principal del dominio.
   - Nombre: `<entidad>_repo_json.py`.
3. Añadir a las entidades los métodos de transformación:
   - `to_dict() -> dict`: serializa la entidad a diccionario.
   - `from_dict(data: dict) -> MiEntidad` (método de clase): reconstruye desde diccionario.
4. Llamar a `guardar` desde `services/` al final de cada operación que modifica datos.
5. Llamar a `cargar` al arrancar la app (en `main.py`) en lugar del seed de datos.
6. Añadir tests con ficheros temporales (`tmp_path` de pytest).

# REGLAS ESTRICTAS PARA HOY

- **Ningún I/O de ficheros en `entities/`**. `to_dict()` y `from_dict()` son aceptables (son transformaciones puras).
- El path del fichero se inyecta como parámetro en el constructor del adaptador, no se hardcodea.
- Usar siempre `pathlib.Path` para los paths.
- Manejar `FileNotFoundError` al cargar: si no existe el fichero, devolver lista vacía.
- No romper los tests existentes; el seed puede coexistir como fallback.

# MODO TUTOR

Muestra `to_dict()` de la entidad principal y cómo guardarlo con `json.dump`. Pide al alumno que implemente `from_dict()` y el adaptador de otra entidad.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion10: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `persistence/` tiene al menos un adaptador JSON por entidad principal
- [ ] `to_dict()` y `from_dict()` implementados en las entidades que se persisten
- [ ] El path del fichero se inyecta en el constructor — no está hardcodeado
- [ ] Tests con `tmp_path` pasan: guardar → cargar devuelve los mismos objetos
- [ ] Al reiniciar la app los datos persisten (verificado manualmente)
- [ ] `FileNotFoundError` manejado: si no existe el fichero, se devuelve lista vacía

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion10.md` y haz commit:

```markdown
# Journal — Sesión 10 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Adaptadores creados
<!-- Lista: entidad → fichero del adaptador → formato elegido -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: elegimos JSON porque es legible y fácil de depurar -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion10.md
git commit -m "sesion10: journal de sesión"
git push origin main
```
