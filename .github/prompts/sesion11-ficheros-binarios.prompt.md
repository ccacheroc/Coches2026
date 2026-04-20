# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 11** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros binarios** usando `pickle`.

# TAREAS DE HOY (WORKFLOW)

1. Crear adaptadores en `persistence/`:
   - `persistence/coches_repo_bin.py`
   - `persistence/personas_repo_bin.py`
2. Usar `pickle.dump` / `pickle.load` para serializar objetos directamente:
   ```python
   import pickle

   def guardar(self, objetos: list) -> None:
       with open(self.__path, "wb") as f:
           pickle.dump(objetos, f)

   def cargar(self) -> list:
       try:
           with open(self.__path, "rb") as f:
               return pickle.load(f)
       except FileNotFoundError:
           return []
   ```
3. Comparar las ventajas/desventajas de pickle vs JSON (documentar en un comentario).
4. Configurar `main.py` para elegir entre adaptador binario y de texto mediante una constante.
5. Añadir tests con `tmp_path` que verifiquen que los objetos se guardan y recuperan correctamente.

# VENTAJAS / DESVENTAJAS a documentar

| | JSON (texto) | Pickle (binario) |
|---|---|---|
| Legible por humanos | ✅ | ❌ |
| Serializa objetos Python directamente | ❌ (requiere `to_dict`) | ✅ |
| Portable entre versiones | ✅ | ⚠️ (depende de la clase) |
| Seguro al cargar datos no confiables | ✅ | ❌ (nunca cargar pickle de fuentes externas) |

# REGLAS ESTRICTAS PARA HOY

- **Nunca** cargar un fichero pickle de una fuente no confiable. Documentarlo con un `# WARNING`.
- Los adaptadores binarios y de texto tienen la misma interfaz; son intercambiables.
- No cambiar las entidades para acomodar pickle (deben ser serializables por defecto).

# MODO TUTOR

Muestra el adaptador de coches binario. Pide al alumno que implemente el de personas y que escriba el test antes de mostrar la solución.

