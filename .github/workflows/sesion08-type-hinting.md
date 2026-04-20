# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 8** de la asignatura.
El objetivo de hoy es añadir **type hinting completo** (PEP 484 / PEP 526) a todo el código.

# TAREAS DE HOY (WORKFLOW)

1. Añadir type hints a **todas** las firmas públicas que aún no los tengan:
   - Parámetros y tipo de retorno en métodos y funciones.
   - Atributos de instancia en `__init__` (anotación explícita o con `self.__x: tipo = ...`).
2. Usar tipos de `typing` donde aplique:
   - `list[Coche]` en lugar de `list` sin anotar.
   - `Coche | None` para opcionales (sintaxis Python 3.10+).
   - `ClassVar[dict[str, float]]` para atributos de clase.
3. Verificar con `mypy` o `pyright` que no hay errores de tipado:
   ```bash
   pip install mypy
   mypy entities/ services/ ui/ --strict
   ```
4. Corregir los errores encontrados sin cambiar la lógica de negocio.
5. Actualizar tests si alguna firma ha cambiado.

# REGLAS ESTRICTAS PARA HOY

- No usar `Any` salvo en `Resultado.valor` (donde es deliberado y debe documentarse).
- No usar `typing.Optional[X]`; usar `X | None` (Python 3.10+).
- No alterar la lógica de negocio; hoy solo se añaden anotaciones.

# MODO TUTOR

Muestra cómo anotar `Coche.__init__` y el atributo de clase `__km_por_marca`. Luego pide al alumno que anote `Persona` y `Concesionario`.

