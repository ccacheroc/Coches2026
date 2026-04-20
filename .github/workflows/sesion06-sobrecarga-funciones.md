# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 6** de la asignatura.
El objetivo de hoy es implementar la **sobrecarga de funciones built-in** de Python: `__str__`, `__repr__`, `__len__`, `__bool__`, etc.

# TAREAS DE HOY (WORKFLOW)

1. Implementar `__str__` en todas las entidades para producir salida legible por el usuario:
   - `Coche`: matrícula, marca y km recorridos.
   - `Persona`: DNI, nombre completo y matrícula del coche (o "sin coche").
   - `Concesionario`: nombre, número de coches y número de clientes.
2. Implementar `__repr__` con información técnica para depuración.
3. Implementar `__len__` en `Concesionario` (devuelve el número de coches en inventario).
4. Implementar `__bool__` en `Resultado` (`True` si `ok`, `False` si error).
5. Implementar `__bool__` en `Coche` (`True` si tiene energía disponible para avanzar).
6. Verificar que `ui/menu.py` usa `str(coche)` y `str(persona)` en lugar de acceder a atributos directamente.
7. Añadir tests para cada dunder implementado.

# REGLAS ESTRICTAS PARA HOY

- `__str__` va en `entities/`; la UI solo llama a `str(objeto)`.
- `__repr__` debe permitir reconstruir el objeto o al menos identificarlo unívocamente.
- No implementar `__eq__` ni `__hash__` hoy (es Sesión 7).

# MODO TUTOR

Muestra el `__str__` de `CocheCombustion` como ejemplo. Pide al alumno que implemente `__repr__` y `__bool__` antes de revelar la solución.

