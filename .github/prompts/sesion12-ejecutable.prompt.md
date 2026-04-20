---
mode: 'agent'
description: 'Sesión 12 — Crear un ejecutable distribuible con PyInstaller'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 12** de la asignatura.
El objetivo de hoy es crear un **ejecutable distribuible** de la aplicación.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

# TAREAS DE HOY (WORKFLOW)

1. Instalar `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Generar el ejecutable en modo `--onefile`:
   ```bash
   pyinstaller --onefile main.py --name nombre-del-proyecto
   ```
3. Verificar que el ejecutable funciona correctamente:
   ```bash
   ./dist/nombre-del-proyecto      # macOS/Linux
   dist\nombre-del-proyecto.exe    # Windows
   ```
4. Añadir al `.gitignore` los artefactos generados:
   ```gitignore
   dist/
   build/
   *.spec
   ```
5. Documentar en `README.md` cómo generar y ejecutar el binario.
6. (Opcional) Configurar el fichero `.spec` para incluir recursos adicionales.

# CONSIDERACIONES

Si la app usa ficheros de datos (pickle/JSON), los paths deben ser relativos al directorio de ejecución, no al directorio del script. Usar `pathlib.Path`:

```python
from pathlib import Path
BASE_DIR = Path(__file__).parent
DATOS_PATH = BASE_DIR / "datos" / "entidades.json"
```

En ejecutables `--onefile`, `__file__` apunta a un directorio temporal. Usar `sys._MEIPASS` si es necesario acceder a recursos empaquetados.

# REGLAS ESTRICTAS PARA HOY

- No subir `dist/` ni `build/` al repositorio.
- El ejecutable debe funcionar sin tener Python instalado en la máquina destino.
- Todos los tests deben pasar antes de generar el ejecutable.

# MODO TUTOR

Guía al alumno paso a paso. Muestra el comando de PyInstaller y pide que lo ejecuten, luego comprueben juntos que el binario arranca correctamente.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion12: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `dist/` y `build/` están en `.gitignore` y no aparecen en `git status`
- [ ] El ejecutable generado arranca correctamente sin Python instalado (probado en otra terminal sin `.venv` activo)
- [ ] `README.md` documenta cómo generar el ejecutable y cómo ejecutarlo en macOS/Linux y Windows
- [ ] Si la app usa ficheros de datos, los paths son correctos dentro del ejecutable

---

# 📓 JOURNAL DE SESIÓN — REFLEXIÓN FINAL DEL CURSO

Al terminar, crea o actualiza `journal/sesion12.md` y haz commit. Esta es la última sesión: incluye también una **reflexión general del curso**:

```markdown
# Journal — Sesión 12 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Pasos para generar el ejecutable
<!-- Documenta el comando exacto y los flags usados -->

## Problemas encontrados y cómo los resolvimos


---

## 🎓 Reflexión final del curso

### ¿Qué concepto OO ha sido el más difícil de entender?


### ¿Qué parte del proyecto estáis más orgullosos?


### ¿Qué cambiaríais si empezarais de nuevo?


### ¿Qué herramientas o prácticas seguiréis usando en el futuro?


## Tiempo invertido en total (todas las sesiones)
- Horas totales estimadas:
```

```bash
git add journal/sesion12.md
git commit -m "sesion12: journal final del curso"
git push origin main
```
