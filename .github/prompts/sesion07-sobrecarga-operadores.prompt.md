# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 7** de la asignatura.
El objetivo de hoy es implementar la **sobrecarga de operadores** matemáticos, de comparación y de acceso por índice.

# TAREAS DE HOY (WORKFLOW)

1. Implementar `__eq__` y `__hash__` en entidades con identidad:
   - `Coche`: igualdad por matrícula.
   - `Persona`: igualdad por DNI.
2. Implementar operadores aritméticos en `Concesionario`:
   - `__add__` / `__iadd__` (`+`, `+=`): añadir un `Coche` al inventario → devuelve nuevo concesionario o muta el actual.
   - `__sub__` / `__isub__` (`-`, `-=`): eliminar un `Coche` por matrícula.
3. Implementar `__getitem__` en `Concesionario` para acceder a coches por índice o matrícula:
   ```python
   concesionario["1234ABC"]  # devuelve el Coche con esa matrícula o None
   concesionario[0]          # devuelve el primer coche del inventario
   ```
4. Implementar `__contains__` (`in`) para comprobar si una matrícula está en el inventario.
5. Añadir tests para cada operador.

# REGLAS ESTRICTAS PARA HOY

- `__eq__` debe ir acompañado siempre de `__hash__` (si el objeto puede estar en sets o dicts).
- Los operadores que mutan el estado (`+=`, `-=`) devuelven `self`.
- Los operadores que crean copias (`+`, `-`) devuelven una **nueva instancia**.
- No romper tests existentes.

# MODO TUTOR

Muestra `__eq__` y `__hash__` de `Coche`. Luego pide al alumno que implemente `__add__` de `Concesionario` antes de mostrar la solución.

