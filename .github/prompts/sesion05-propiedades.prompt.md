# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 5** de la asignatura.
El objetivo de hoy es enriquecer el diseño con **propiedades (`@property`)**, **herencia múltiple** y **clases abstractas** donde proceda.

# TAREAS DE HOY (WORKFLOW)

1. Convertir `Coche` en clase abstracta con `ABC` y decorar `avanzar` con `@abstractmethod`.
2. Añadir `@property` de lectura a los atributos que necesita la capa `services` o `ui`:
   - `matricula`, `marca`, `kilometros_recorridos` en `Coche`.
   - `gasolina` en `CocheCombustion`.
   - `bateria_kwh` en `CocheElectrico`.
   - `dni`, `nombre`, `coche` en `Persona`.
3. Añadir setter `@coche.setter` en `Persona` (con validación mínima).
4. Implementar `CocheHibrido` con herencia múltiple real de `CocheCombustion` y `CocheElectrico`.
   - Definir orden MRO explícito: `CocheHibrido(CocheElectrico, CocheCombustion)`.
   - `avanzar` prioriza batería; si no hay suficiente, usa gasolina.
5. Actualizar diagrama de clases (ver skill `skills/mermaid-class-diagram.md`).
6. Asegurarse de que los tests existentes siguen pasando.

# REGLAS ESTRICTAS PARA HOY

- `Coche` no puede instanciarse directamente; debe lanzar `TypeError` si se intenta.
- No añadir setter si no hay validación real. Consulta `instructions/oo-design.instructions.md`.
- El orden MRO en `CocheHibrido` debe ser explícito y documentado con un comentario.

# MODO TUTOR

Muestra cómo declarar `Coche` como abstracta. Luego pide al alumno que identifique qué `@property` son necesarias antes de implementarlas.

