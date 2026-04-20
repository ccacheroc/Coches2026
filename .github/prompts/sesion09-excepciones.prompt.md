# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 9** de la asignatura.
El objetivo de hoy es añadir **manejo de excepciones** propio del dominio.

# TAREAS DE HOY (WORKFLOW)

1. Crear una jerarquía de excepciones propias en `entities/excepciones.py`:
   ```python
   class CochesAppError(Exception): ...
   class MatriculaInvalidaError(CochesAppError): ...
   class SinEnergiaError(CochesAppError): ...
   class DniInvalidoError(CochesAppError): ...
   class CocheOcupadoError(CochesAppError): ...
   ```
2. Lanzar estas excepciones en `__init__` para invariantes de construcción
   (ej. matrícula vacía, DNI con formato incorrecto).
3. **Mantener `Resultado`** para errores de flujo de negocio esperados (sin energía, coche ya asignado).
   Las excepciones propias son para **bugs de programación** o **datos de entrada inválidos** en la construcción.
4. Capturar excepciones en `ui/menu.py` y mostrar mensaje amigable al usuario.
5. Añadir tests que verifiquen que las excepciones se lanzan en los casos correctos.

# CRITERIO: excepción vs Resultado

| Situación | Mecanismo |
|---|---|
| Matrícula vacía al construir `Coche` | `raise MatriculaInvalidaError` |
| `avanzar` con energía insuficiente | `return Resultado.error(...)` |
| DNI con formato incorrecto en `Persona.__init__` | `raise DniInvalidoError` |
| Transferir coche ya asignado | `return Resultado.error(...)` |

# REGLAS ESTRICTAS PARA HOY

- Las excepciones del dominio heredan de `CochesAppError`, no directamente de `Exception`.
- `services/` no lanza excepciones propias; las deja propagar o las convierte en `Resultado`.
- `ui/` captura excepciones y las muestra como mensajes de error sin stack trace.

# MODO TUTOR

Muestra cómo crear `CochesAppError` y `MatriculaInvalidaError`. Pide al alumno que añada la validación en `Coche.__init__` antes de mostrar la solución.

