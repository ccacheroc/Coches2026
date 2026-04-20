# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 10** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros de texto plano** (CSV / JSON / TXT).

# TAREAS DE HOY (WORKFLOW)

1. Decidir el formato de serialización (recomendado: JSON por legibilidad). Documentar la decisión.
2. Crear adaptadores en `persistence/`:
   - `persistence/coches_repo_txt.py`: guarda y carga la lista de coches.
   - `persistence/personas_repo_txt.py`: guarda y carga la lista de personas.
3. Los adaptadores implementan una interfaz simple (aunque no sea ABC formal todavía):
   ```python
   def guardar(self, datos: list[dict]) -> None: ...
   def cargar(self) -> list[dict]: ...
   ```
4. Convertir entidades a `dict` para serializar (método `to_dict()`) y reconstruirlas desde `dict` (método de clase `from_dict()`).
5. Llamar a `guardar` desde `services/` al final de cada operación que modifica datos.
6. Llamar a `cargar` al arrancar la app (en `main.py`) en lugar del seed de datos.
7. Añadir tests con ficheros temporales (`tmp_path` de pytest).

# REGLAS ESTRICTAS PARA HOY

- **Ningún I/O de ficheros en `entities/`**. `to_dict()` y `from_dict()` sí son aceptables (son transformaciones puras).
- El path del fichero se inyecta como parámetro, no se hardcodea.
- Manejar `FileNotFoundError` al cargar: si no existe el fichero, devolver lista vacía.
- No romper los tests existentes; el seed puede coexistir como fallback.

# MODO TUTOR

Muestra `to_dict()` de `Coche` y cómo guardarlo con `json.dump`. Pide al alumno que implemente `from_dict()` y el adaptador de personas.

