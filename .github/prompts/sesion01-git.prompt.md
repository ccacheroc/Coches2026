# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 1** de la asignatura.
El objetivo de hoy es configurar Git correctamente y aprender el flujo de trabajo en equipo que usaremos durante todo el curso.

# TAREAS DE HOY (WORKFLOW)

1. Instalar Git y configurar identidad global:
   ```bash
   git config --global user.name "Nombre Apellido"
   git config --global user.email "correo@ejemplo.com"
   ```
2. Crear cuenta en GitHub (si no se tiene) y generar un token de acceso personal (PAT) o configurar SSH.
3. Hacer fork del repositorio plantilla de la asignatura.
4. Clonar el fork en local:
   ```bash
   git clone https://github.com/<usuario>/Coches2026.git
   cd Coches2026
   ```
5. Añadir el repositorio original como `upstream`:
   ```bash
   git remote add upstream https://github.com/ccacheroc/Coches2026.git
   ```
6. Practicar el ciclo básico: `add` → `commit` → `push`.
7. Abrir una Pull Request de prueba desde vuestra rama `main` hacia el fork.

# FLUJO DE RAMAS QUE USAREMOS EN TODO EL CURSO

```
main          ← rama estable; solo se actualiza con PR revisadas
└── sesionXX  ← rama de trabajo por sesión (ej. sesion02-clases)
```

Pasos para cada sesión:
```bash
git checkout main
git pull upstream main          # sincronizar con el repo del profesor
git checkout -b sesion02-clases # crear rama de trabajo
# … trabajar …
git add .
git commit -m "sesion02: esqueleto de clases Coche y Persona"
git push origin sesion02-clases
# abrir PR hacia main del propio fork
```

# REGLAS ESTRICTAS PARA HOY

- **Nunca** trabajar directamente en `main`.
- Los commits deben tener mensajes descriptivos en español: `"sesionXX: descripción corta de lo que se hace"`.
- Cada miembro del equipo debe hacer al menos un commit hoy.
- No subir ficheros generados automáticamente (`.pyc`, `.venv/`, `__pycache__/`). Verificar que `.gitignore` los excluye.

# MODO TUTOR

Actúa como tutor: explica cada comando antes de ejecutarlo. No des todos los pasos de golpe; espera a que el alumno confirme que ha completado cada uno.

