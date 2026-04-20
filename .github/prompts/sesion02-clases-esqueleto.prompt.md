---
mode: 'agent'
description: 'Sesión 2 — Descubrir el dominio, diseñar el diagrama de clases y crear los esqueletos en src/'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 2** de la asignatura.
El objetivo de hoy es descubrir el dominio del sistema que el equipo quiere implementar, diseñar el diagrama de clases inicial y crear los esqueletos de clase en `src/entities/`.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

> 🎓 **Modo de trabajo**: esta sesión es completamente **socrática**. El agente NO genera el diseño
> por el alumno — hace preguntas para que sea el alumno quien lo descubra.
> El agente crea **un ejemplo** de cada artefacto y luego guía al alumno para que construya el resto.

---

# ESTRUCTURA DE CARPETAS OBJETIVO

Todo el código fuente reside bajo `src/`, organizado según la arquitectura de cuatro capas:

```
src/
├── main.py               ← punto de entrada; construye dependencias y lanza la UI
├── entities/             ← dominio puro (sin I/O)
│   ├── __init__.py
│   └── resultado.py      ← debe existir con Resultado.exito / Resultado.error
├── services/             ← casos de uso; orquesta entidades
│   └── __init__.py
├── ui/                   ← interfaz de consola
│   └── __init__.py
└── persistence/          ← adaptadores de almacenamiento (reservado)
    └── __init__.py
tests/                    ← tests por capa (fuera de src/)
    └── __init__.py
```

Ver `instructions/architecture.instructions.md` para las reglas de dependencias entre capas.

---

# FASE 1 — DESCUBRIR EL DOMINIO (socrático)

## Paso 1.1 — Preguntar qué sistema quiere implementar el equipo

Empezar con esta pregunta abierta:

> *"¿Qué sistema queréis implementar? Describidlo en una o dos frases, como si se lo
> explicarais a alguien que no sabe nada de programación."*

Escuchar la respuesta antes de continuar.

## Paso 1.2 — Clarificar el alcance con preguntas socráticas

A partir de la descripción del alumno, hacer **una pregunta a la vez** para clarificar el alcance.
No pasar a la siguiente pregunta hasta recibir respuesta. Ejemplos de preguntas orientativas
(adaptarlas al dominio concreto que describa el alumno):

- *"¿Qué 'cosas' principales maneja vuestro sistema? ¿Podéis listarlas?"*
- *"De todas esas cosas, ¿cuáles tienen datos propios que el sistema necesita recordar?"*
- *"¿Hay alguna relación entre ellas? Por ejemplo, ¿una pertenece a otra, o una contiene varias?"*
- *"¿Qué operaciones puede hacer el usuario con el sistema?"*
- *"¿Hay alguna restricción importante? Por ejemplo, ¿puede haber duplicados? ¿Hay límites?"*

Continuar preguntando hasta tener suficiente información para identificar las clases principales
y sus atributos. Como mínimo deben quedar claros:
- Las **3-5 clases principales** del dominio.
- Los **atributos de instancia** más importantes de cada una (nombre y tipo aproximado).
- Si hay algún **atributo de clase** (dato compartido por todas las instancias).

## Paso 1.3 — Confirmar la comprensión antes de continuar

Antes de pasar al diagrama, hacer un resumen de lo entendido y pedir confirmación:

> *"Hasta aquí he entendido lo siguiente: [resumen]. ¿Es correcto? ¿Falta algo importante
> o hay algo que queráis cambiar antes de empezar a diseñar?"*

---

# FASE 2 — DIAGRAMA DE CLASES Y README (socrático)

## Paso 2.1 — Guiar al alumno para identificar las clases

No dar las clases directamente. Preguntar:

> *"A partir de lo que me habéis contado, ¿qué nombres de clase propondríais?
> Recordad que las clases representan 'cosas' del dominio, no acciones."*

Si el alumno tiene dificultades, dar una pista con la primera clase como ejemplo
y pedir que proponga las demás.

## Paso 2.2 — Guiar para identificar atributos de instancia y de clase

Para cada clase identificada, preguntar:

> *"Para la clase [Nombre], ¿qué datos necesita guardar cada objeto individualmente?
> ¿Y hay algún dato que sea el mismo para todos los objetos de esa clase?"*

Recordar las reglas de visibilidad:
- Los atributos de instancia serán **privados** (`self.__nombre`).
- Los atributos de clase llevan `ClassVar`.

## Paso 2.3 — Generar el diagrama Mermaid y actualizar el README

Con las clases y atributos confirmados por el alumno, actualizar `README.md` con:
1. Una breve descripción del sistema (2-3 líneas).
2. El diagrama de clases en Mermaid, siguiendo `instructions/mermaid.instructions.md`.

Mostrar el diagrama al alumno y preguntar:

> *"¿Refleja bien lo que teníais en mente? ¿Hay alguna clase o atributo que falte
> o que no sea correcto?"*

Iterar hasta que el alumno valide el diagrama.

---

# FASE 3 — ESQUELETOS DE CLASE EN `src/entities/` (socrático)

## Paso 3.1 — El agente crea el esqueleto de la clase principal como ejemplo

Crear **una sola clase** (la más representativa del dominio) con:
- `__init__` con atributos privados anotados con type hints.
- `__str__` básico.
- Sin métodos de negocio (eso es Sesión 3).
- Sin herencia (eso es Sesión 4).

Mostrarla al alumno y explicar brevemente cada decisión.

## Paso 3.2 — El alumno implementa el resto

Pedir al alumno que implemente las demás clases siguiendo el mismo patrón:

> *"Ahora es vuestro turno. Implementad el esqueleto de [siguiente clase].
> Cuando lo tengáis, mostradme el código y os doy feedback antes de continuar."*

Revisar cada clase que presente el alumno y dar feedback específico:
- ¿Los atributos son privados (`self.__nombre`)?
- ¿Tiene type hints en `__init__`?
- ¿El `__str__` es informativo?
- ¿Existe `entities/resultado.py` con `Resultado.exito` y `Resultado.error`?

No pasar a la siguiente clase hasta que la actual esté bien.

## Paso 3.3 — Crear los `__init__.py` necesarios

Asegurarse de que todos los paquetes tienen su `__init__.py`.

---

# FASE 4 — TESTS TDD MÍNIMOS (socrático)

## Paso 4.1 — El agente muestra un test de construcción como ejemplo

Crear el test de construcción de la clase principal en `tests/test_entities.py`:

```python
def test_[clase]_se_crea_correctamente():
    # Given / When
    obj = MiClase("param1", "param2")

    # Then
    assert str(obj) != ""
```

## Paso 4.2 — El alumno escribe los tests del resto de clases

> *"Escribid ahora el test de construcción para [siguiente clase].
> Recordad la estructura Given/When/Then."*

Verificar que `python -m pytest -q` pasa antes de continuar.

---

# FASE 5 — ESQUELETOS DE SERVICIOS Y `main.py` (socrático)

## Paso 5.1 — Preguntar qué operaciones principales necesita el sistema

> *"Pensad en las operaciones principales que un usuario querría hacer con vuestro sistema.
> Por ejemplo: dar de alta, listar, buscar, eliminar... ¿Cuáles son las más importantes?"*

## Paso 5.2 — El agente crea el esqueleto de un servicio como ejemplo

Crear **un servicio** (el más representativo) en `src/services/` con:
- Método(s) esqueleto que devuelvan `Resultado`.
- Inyección de dependencias en `__init__`.
- Sin lógica de negocio todavía — solo `pass` o `return Resultado.exito("TODO")`.

```python
from entities.resultado import Resultado

class GestionXxxService:
    """Orquesta las operaciones sobre Xxx."""

    def __init__(self, ...) -> None:
        ...

    def registrar(self, ...) -> Resultado:
        """TODO: implementar en sesión 3."""
        return Resultado.exito("TODO")
```

## Paso 5.3 — El alumno crea los demás servicios

> *"Siguiendo este patrón, cread el servicio para [siguiente entidad].
> Mostradme el código cuando lo tengáis."*

## Paso 5.4 — Actualizar `src/main.py`

Actualizar `src/main.py` para que construya las dependencias y demuestre que la arquitectura
funciona de extremo a extremo (aunque sea con datos hardcodeados):

```python
from services.gestion_xxx_service import GestionXxxService
from entities.xxx import Xxx

def main() -> None:
    servicio = GestionXxxService(...)
    resultado = servicio.registrar(...)
    print(resultado.mensaje)

if __name__ == "__main__":
    main()
```

Verificar que `python src/main.py` arranca sin errores.

---

# FASE 6 — REVISIÓN FINAL Y FEEDBACK

Cuando el alumno indique que ha terminado, realizar una revisión completa y dar
**feedback sincero y honesto** sobre los siguientes aspectos:

## Checklist de revisión del agente

**Diseño:**
- ¿Las clases tienen nombres claros en PascalCase que representan conceptos del dominio?
- ¿Los atributos de instancia son todos privados (`self.__nombre`)?
- ¿Se han identificado correctamente los atributos de clase (si los hay)?
- ¿El diagrama Mermaid en README.md refleja fielmente el código?

**Código:**
- ¿Todos los `__init__` tienen type hints en parámetros y atributos?
- ¿Todos los `__str__` son informativos y sin acceso a datos de otras clases?
- ¿Los servicios reciben sus dependencias por inyección (no las crean internamente)?
- ¿`resultado.py` implementa correctamente `Resultado.exito` y `Resultado.error`?

**Tests:**
- ¿Existe al menos un test de construcción por clase?
- ¿`python -m pytest -q` pasa con 0 fallos?

**Arquitectura:**
- ¿`grep -r "from entities" src/ui/` devuelve vacío?
- ¿`python src/main.py` arranca sin errores?

## Formato del feedback

```
✅ Puntos fuertes:
   - [lo que han hecho bien, con ejemplos concretos]

⚠️  Aspectos a mejorar:
   - [lo que no está del todo bien, con explicación del por qué y cómo corregirlo]

🔴 Errores que hay que corregir antes de cerrar la sesión:
   - [violaciones de las reglas — el alumno debe corregirlas ahora]
```

Si hay errores en rojo, no dar la sesión por terminada hasta que estén corregidos.

---

# REGLAS ESTRICTAS PARA HOY

- Los atributos de dominio son privados (`self.__nombre`). Ver `instructions/entities.instructions.md`.
- No implementar lógica de negocio todavía — solo estructura.
- No añadir `@property` todavía salvo que sean imprescindibles para los tests.
- `ui/` no importa nada de `entities/`.
- `entities/resultado.py` debe existir antes de crear los servicios.

---

# ✅ DEFINITION OF DONE (DoD)

Antes de cerrar la sesión, verifica que se cumplen **todos** los criterios:

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python src/main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `src/ui/`: `grep -r "from entities" src/ui/` → vacío
- [ ] Commits del día con patrón `sesion02: descripción corta`

## Quality gates específicos de esta sesión
- [ ] El alumno ha descrito el sistema y el agente lo ha confirmado antes de diseñar
- [ ] Al menos 3 clases de dominio creadas en `src/entities/`
- [ ] Todos los atributos de instancia son `self.__privado` (doble guion) con type hints
- [ ] `src/entities/resultado.py` existe con `Resultado.exito` y `Resultado.error`
- [ ] `__str__` implementado en todas las clases nuevas
- [ ] Al menos un test de construcción por clase in `tests/test_entities.py`
- [ ] Al menos un servicio esqueleto creado en `src/services/`
- [ ] `src/main.py` usa los servicios y arranca sin errores
- [ ] Diagrama de clases Mermaid actualizado en `README.md` y validado por el alumno
- [ ] El agente ha dado feedback final y el alumno ha corregido los errores en rojo

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion02.md` y haz commit:

```markdown
# Journal — Sesión 02 — [fecha]

## Integrantes
-
-

## Sistema elegido
<!-- Describe en 2-3 frases el sistema que vais a implementar -->

## Clases identificadas y atributos principales
<!-- Lista las clases creadas y sus atributos más relevantes -->
<!-- Ej: Producto — __nombre: str, __precio: float, __stock: int -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: decidimos que X es privado porque modificarlo directamente rompería... -->

## Problemas encontrados y cómo los resolvimos


## Feedback recibido del agente
<!-- Resume los puntos fuertes y las mejoras indicadas -->

## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion02.md
git commit -m "sesion02: journal de sesión"
git push origin main
```
