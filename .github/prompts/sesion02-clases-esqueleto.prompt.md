# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 2** de la asignatura.
El objetivo de hoy es diseñar el diagrama de clases inicial de nuestra app y crear los esqueletos de clase en Python.

# TAREAS DE HOY (WORKFLOW)

1. A partir de la idea del concesionario, identificar las clases principales: `Coche`, `Persona`, `Concesionario`.
2. Definir los **atributos de instancia** de cada clase (con tipo y visibilidad).
3. Definir si hay **atributos de clase** (compartidos por todas las instancias).
4. Generar el diagrama de clases en Mermaid (ver skill `skills/mermaid-class-diagram.md`).
5. Implementar los esqueletos de clase en `entities/`:
   - Solo `__init__` con atributos privados.
   - Sin métodos de negocio todavía (eso es Sesión 3).
   - Sin herencia todavía (eso es Sesión 4).
6. Añadir `__str__` básico para poder imprimir objetos en la consola.
7. Crear tests mínimos que comprueben que los objetos se crean correctamente.

# REGLAS ESTRICTAS PARA HOY

- Todos los atributos de dominio son privados (`self.__nombre`). Consulta `instructions/oo-design.instructions.md`.
- No implementes lógica de negocio todavía; solo la estructura.
- No añadas `@property` todavía salvo que sean imprescindibles para los tests.
- El fichero `entities/resultado.py` debe existir con `Resultado.exito` y `Resultado.error`.

# MODO TUTOR

Empieza proponiendo la clase `Coche` con sus atributos. Luego pide al alumno que implemente `Persona` y `Concesionario` por su cuenta antes de mostrar la solución.

