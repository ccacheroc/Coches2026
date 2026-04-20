# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 3** de la asignatura.
El objetivo de hoy es enriquecer el diagrama de clases y el código con **métodos de instancia y de clase**.

# TAREAS DE HOY (WORKFLOW)

1. Revisar el diagrama de clases actual e identificar qué comportamientos faltan.
2. Añadir **métodos de instancia** a cada entidad:
   - `Coche`: `avanzar(km)` que descuente energía y acumule kilómetros.
   - `Persona`: `asignar_coche(coche)`, `liberar_coche()`.
   - `Concesionario`: `anadir_coche(coche)`, `anadir_cliente(persona)`, `eliminar_coche(matricula)`, `eliminar_cliente(dni)`.
3. Añadir **métodos de clase** donde aplique:
   - `Coche.obtener_km_por_marca(marca)` — acumulado global por marca usando atributo de clase.
4. Todas las operaciones que pueden fallar devuelven `Resultado`. Ver `instructions/architecture.instructions.md`.
5. Actualizar el diagrama Mermaid en `README.md` (ver skill `skills/mermaid-class-diagram.md`).
6. Escribir/ampliar tests con Given/When/Then para cada método nuevo.

# REGLAS ESTRICTAS PARA HOY

- Ningún método en `entities/` puede contener `print()` ni `input()`.
- Los métodos de clase se decoran con `@classmethod` y reciben `cls` como primer parámetro.
- No añadir herencia todavía (es Sesión 4).
- `Resultado` es obligatorio para toda operación que pueda fallar.

# MODO TUTOR

Muestra el método `avanzar` de `Coche` como ejemplo. Luego pide al alumno que implemente `repostar` o `recargar` antes de mostrar tu solución.

