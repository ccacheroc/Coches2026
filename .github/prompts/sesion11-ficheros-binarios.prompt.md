---
mode: 'agent'
description: 'Sesión 11 — Añadir persistencia en ficheros binarios (pickle)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 11** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros binarios** usando `pickle`.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Crear adaptadores binarios en `persistence/`:
   - Nombre: `<entidad>_repo_bin.py`.
2. Usar `pickle.dump` / `pickle.load` para serializar objetos directamente:
   ```python
   import pickle
   from pathlib import Path

   class EntidadRepoBin:
       def __init__(self, path: Path) -> None:
           self.__path = path

       def guardar(self, entidades: list) -> None:
           with open(self.__path, "wb") as f:
               pickle.dump(entidades, f)

       def cargar(self) -> list:
           try:
               with open(self.__path, "rb") as f:
                   return pickle.load(f)
           except FileNotFoundError:
               return []
   ```
3. Comparar ventajas/desventajas de pickle vs JSON (documentar en un comentario):

   | | JSON (texto) | Pickle (binario) |
   |---|---|---|
   | Legible por humanos | ✅ | ❌ |
   | Serializa objetos Python directamente | ❌ (requiere `to_dict`) | ✅ |
   | Portable entre versiones | ✅ | ⚠️ |
   | Seguro con datos no confiables | ✅ | ❌ |

4. Configurar `main.py` para elegir entre adaptador binario y de texto mediante una constante.
5. Añadir tests con `tmp_path` que verifiquen que los objetos se guardan y recuperan correctamente.

# REGLAS ESTRICTAS PARA HOY

- **Nunca** cargar un fichero pickle de una fuente no confiable. Documentarlo con `# WARNING`.
- Los adaptadores binarios y de texto tienen la misma interfaz (`guardar` / `cargar`); son intercambiables.
- No cambiar las entidades para acomodar pickle (deben ser serializables por defecto).

# MODO TUTOR

Muestra el adaptador binario de la entidad principal. Pide al alumno que implemente el de otra entidad y que escriba el test antes de mostrar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion11: descripción corta`

## Quality gates específicos de esta sesión
- [ ] Adaptadores binarios con la misma interfaz (`guardar` / `cargar`) que los de texto — son intercambiables
- [ ] `# WARNING` presente antes de `pickle.load` en todos los adaptadores binarios
- [ ] Tests con `tmp_path` pasan para los adaptadores binarios
- [ ] `main.py` tiene una constante o flag para elegir entre formato JSON y Pickle
- [ ] Las entidades se serializan/deserializan correctamente sin modificar su código

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion11.md` y haz commit:

```markdown
# Journal — Sesión 11 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Adaptadores binarios creados
<!-- Lista: entidad → fichero del adaptador binario -->

## Comparativa JSON vs Pickle en vuestro proyecto
<!-- ¿Cuál usaríais en producción y por qué? -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion11.md
git commit -m "sesion11: journal de sesión"
git push origin main
```
