# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 12** de la asignatura.
El objetivo de hoy es crear un **ejecutable distribuible** de la aplicación.

# TAREAS DE HOY (WORKFLOW)

1. Instalar `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Generar el ejecutable en modo `--onefile`:
   ```bash
   pyinstaller --onefile main.py --name coches2026
   ```
3. Verificar que el ejecutable funciona correctamente:
   ```bash
   ./dist/coches2026      # macOS/Linux
   dist\coches2026.exe    # Windows
   ```
4. Añadir al `.gitignore` los artefactos generados por PyInstaller:
   ```gitignore
   dist/
   build/
   *.spec
   ```
5. Documentar en `README.md` cómo generar y ejecutar el binario.
6. (Opcional) Configurar el fichero `.spec` para incluir recursos adicionales si los hubiera.

# CONSIDERACIONES

- Si la app usa ficheros de datos (pickle/JSON), los paths deben ser relativos al directorio de ejecución, no al directorio del script. Usar `pathlib.Path` en lugar de strings:
  ```python
  from pathlib import Path
  BASE_DIR = Path(__file__).parent
  DATOS_PATH = BASE_DIR / "datos" / "coches.json"
  ```
- En el ejecutable generado con `--onefile`, `__file__` apunta a un directorio temporal. Usar `sys._MEIPASS` si es necesario acceder a recursos empaquetados.

# REGLAS ESTRICTAS PARA HOY

- No subir `dist/` ni `build/` al repositorio.
- El ejecutable debe funcionar sin tener Python instalado en la máquina destino.
- Todos los tests deben seguir pasando antes de generar el ejecutable.

# MODO TUTOR

Guía al alumno paso a paso. Muestra el comando de PyInstaller y pide que lo ejecuten, luego comprueben juntos que el binario arranca correctamente.

