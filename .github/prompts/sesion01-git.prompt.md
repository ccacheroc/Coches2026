---
mode: 'agent'
description: 'Sesión 1 — Configurar Git, unirse a GitHub Classroom y hacer el primer commit'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 1** de la asignatura.
El objetivo de hoy es configurar Git, unirse a la clase en GitHub Classroom, crear el grupo de trabajo y hacer el primer commit del proyecto.

> ⚠️ En esta asignatura **trabajamos directamente sobre `main`**, sin ramas de trabajo. Todos los commits van a `main`.

---

# TAREAS DE HOY (WORKFLOW)

## 1. Instalar Git y configurar la identidad global

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
```

> ⚠️ **Importante**: el correo debe estar dado de alta en vuestra cuenta de GitHub
> (`github.com → Settings → Emails`). Si no coincide, vuestros commits no se
> reconocerán como vuestros y no aparecerán en el historial de contribuciones.

Verificar la configuración:
```bash
git config --global --list
```

## 2. Unirse a la clase en GitHub Classroom

1. Abrir el enlace de invitación proporcionado por el profesor:
   ```
   https://classroom.github.com/a/[id_repositorio]
   ```
2. Iniciar sesión con vuestra cuenta de GitHub si aún no lo habéis hecho.
3. **Vincular vuestro usuario de GitHub** con vuestro nombre en la lista de la clase
   (GitHub Classroom mostrará el listado del profesor — buscad vuestro nombre y seleccionadlo).

## 3. Crear o unirse a un grupo

- Si sois los **primeros de vuestro equipo** en acceder: crear un grupo nuevo con el nombre acordado (ej. `equipo-01`).
- Si vuestro compañero ya ha creado el grupo: buscadlo en la lista y uníos a él.

> GitHub Classroom creará automáticamente un repositorio **privado** para el grupo
> con la plantilla base de la asignatura.

> 📢 **Revisión por pares**: el día de la revisión por pares deberéis cambiar la visibilidad
> del repositorio a **público** para que vuestros compañeros puedan acceder al código.
> `github.com → [repo] → Settings → Danger Zone → Change repository visibility → Public`
> Recordad volver a **privado** después si lo deseáis.


## 4. Generar un token de acceso personal (PAT)

Para autenticarse desde PyCharm **usad siempre un PAT** (el login vía OAuth desde PyCharm puede dar errores).

1. En GitHub: `Settings → Developer settings → Personal access tokens → Tokens (classic)`.
2. Clic en **Generate new token (classic)**.
3. Nombre: `pycharm-asignatura`.
4. Expiración: al menos hasta el final del curso.
5. Permisos mínimos necesarios: `repo` (acceso completo a repositorios).
6. Copiar el token generado y guardarlo en un lugar seguro — GitHub no lo vuelve a mostrar.

## 5. Clonar el repositorio del grupo desde PyCharm

1. En PyCharm: `File → New Project from VCS` (o `Git → Clone`).
2. URL: la del repositorio creado por GitHub Classroom para vuestro grupo
   (visible en `github.com/[organización]/[nombre-repo-grupo]`).
3. Cuando pida credenciales: usuario de GitHub + **el PAT como contraseña**.

O desde terminal:
```bash
git clone https://github.com/<organización>/<nombre-repo-grupo>.git
cd <nombre-repo-grupo>
```

## 6. Crear, si aún no lo habíais creado, el entorno virtual de Python

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows
pip install pytest
```

## 7. Crear el fichero `.gitignore`

Crear `.gitignore` en la raíz del proyecto con al menos el siguiente contenido:

```gitignore
# Entorno virtual
.venv/

# PyCharm
.idea/
*.iml

# Python
__pycache__/
*.py[cod]
*.pyo
.pytest_cache/

# Artefactos de build
dist/
build/
*.egg-info/
```

## 8. Crear la estructura inicial del proyecto

Crear la carpeta `src/` con un fichero `main.py` mínimo:

```bash
mkdir src
```

Contenido de `src/main.py`:

```python
def main():
    print("¡Hola, mundo!")

if __name__ == "__main__":
    main()
```

Verificar que funciona:

```bash
python src/main.py
```

## 9. Primer miembro del equipo: hacer el primer commit

```bash
git add .gitignore src/main.py
git commit -m "sesion01: añadir .gitignore y estructura inicial del proyecto"
git push origin main
```

> El **segundo miembro** del equipo debe confirmar que ve el commit en GitHub
> y que puede hacer `git pull` sin errores.

Cada miembro debe hacer al menos un commit hoy. El segundo puede añadir, por ejemplo, un `README.md` inicial:
```bash
git pull origin main              # sincronizar antes de crear ficheros nuevos
# ... crear o editar un fichero ...
git add .
git commit -m "sesion01: primer commit de [nombre]"
git push origin main
```

> ⚠️ Si dos personas modifican el mismo fichero a la vez pueden aparecer conflictos.
> Resolved siempre con `git pull` antes de `git push`.

---

# REGLAS ESTRICTAS PARA TODA LA ASIGNATURA

- **Trabajamos sobre `main` directamente** — no hay ramas de trabajo en esta asignatura.
- Los mensajes de commit siguen el patrón: `"sesionXX: descripción corta en español"`.
- Hacer `git pull origin main` **antes** de empezar a trabajar en cada sesión.
- Hacer `git push origin main` **al terminar** cada sesión para que el compañero tenga el código actualizado.
- Nunca subir `.venv/`, `.idea/` ni `__pycache__/` — el `.gitignore` de hoy lo impide.

# MODO TUTOR

Actúa como tutor: explica cada paso antes de ejecutarlo. Espera a que el alumno confirme que ha completado cada uno antes de continuar. Si algo falla, ayuda a diagnosticar el error antes de pasar al siguiente paso.

---

# ✅ DEFINITION OF DONE (DoD)

Antes de cerrar la sesión, verifica que se cumplen **todos** los criterios:

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python main.py` arranca sin errores (o el proyecto base corre)
- [ ] Los commits del día siguen el patrón `sesion01: descripción corta`
- [ ] No hay ficheros innecesarios subidos (`.venv/`, `__pycache__/`, `.idea/`)
- [ ] Cada miembro del equipo tiene al menos un commit visible en GitHub

## Quality gates específicos de esta sesión
- [ ] `git config --global user.email` devuelve un correo dado de alta en GitHub
- [ ] El repositorio del grupo es visible en la organización de GitHub Classroom
- [ ] Ambos miembros aparecen como colaboradores del repositorio
- [ ] `.gitignore` existe en la raíz y excluye `.venv/`, `.idea/` y `__pycache__/`
- [ ] `src/main.py` existe y `python src/main.py` imprime `¡Hola, mundo!`
- [ ] `git log --oneline` muestra al menos 1 commit de cada miembro
- [ ] `git status` muestra `nothing to commit, working tree clean` al final
- [ ] ⏰ **Pendiente para el día de revisión por pares**: cambiar visibilidad del repo a público en `Settings → Danger Zone`

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea el fichero `journal/sesion01.md`, rellénalo y haz commit:

```markdown
# Journal — Sesión 01 — [fecha]

## Integrantes
- [nombre] — GitHub: @[usuario]
- [nombre] — GitHub: @[usuario]

## ¿Qué hemos hecho hoy?


## Decisiones tomadas (y por qué)
<!-- Ej: elegimos PAT en lugar de SSH porque... -->

## Problemas encontrados y cómo los resolvimos
<!-- Ej: el correo no coincidía con GitHub → lo añadimos en Settings → Emails -->

## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion01.md
git commit -m "sesion01: journal de sesión"
git push origin main
```
