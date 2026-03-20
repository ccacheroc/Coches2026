# Especificación del producto: sistema de gestión de coches, personas y concesionario

## 1. Objetivo

Construir una aplicación sencilla orientada a objetos para gestionar:

- Vehículos (`CocheCombustion`, `CocheElectrico`, `CocheHibrido`)
- Personas propietarias de vehículos
- Un concesionario con inventario de coches y base de clientes



---

## 2. Alcance funcional

### 2.1 Vehículos

Se modelará una jerarquía de vehículos con una clase base abstracta `Coche` y tres variantes concretas:

- `CocheCombustion`
- `CocheElectrico`
- `CocheHibrido`

### 2.2 Personas

Se modelará la clase `Persona` con datos de identificación y la posibilidad de poseer un coche.

### 2.3 Concesionario

Se modelará la clase `Concesionario` como agregador principal del dominio, con:

- nombre
- lista de coches
- lista de personas clientes

---

## 3. Requisitos funcionales detallados

## 3.1 Clase abstracta `Coche`

### Responsabilidad
Representar el comportamiento común de cualquier coche.

### Atributos comunes
- `matricula`: identificador único del coche
- `marca`: marca del coche
- `kilometros_recorridos`: kilómetros acumulados por ese coche

### Atributo de clase
- acumulador de kilómetros recorridos por marca para todos los coches de la misma marca

### Reglas
- La clase será abstracta.
- Los atributos estarán encapsulados con el nivel más restrictivo posible.
- Se expondrán únicamente propiedades de lectura y los métodos públicos necesarios.
- `matricula` y `marca` se informan al crear el coche.
- `kilometros_recorridos` comienza en `0`.

### Comportamientos comunes
- consultar datos del coche
- obtener representación legible (`__str__`)
- obtener representación técnica (`__repr__`)
- consultar kilómetros acumulados por marca mediante un método de clase

### Método de clase
`obtener_kilometros_por_marca(marca)`

Devuelve el total acumulado de kilómetros recorridos por todos los coches de esa marca.

### Abstracción y duplicación mínima
Se priorizará **duplicación mínima**. Por tanto, la lógica común de avance y acumulación debe vivir en `Coche` siempre que sea posible, y las subclases solo aportarán la parte específica de su fuente de energía.

La opción preferida es que `Coche` defina la plantilla del avance y que las subclases implementen los métodos abstractos necesarios para:

- comprobar si hay energía suficiente
- consumir energía
- identificar el tipo de energía usado

---

## 3.2 `CocheCombustion`

### Responsabilidad
Representar un coche que utiliza gasolina.

### Atributos específicos
- `gasolina`: litros disponibles, inicializados a `0`

### Consumo
- `0.05` litros por kilómetro

### Métodos públicos
- `repostar(litros)`
- `avanzar(km)`

### Reglas de negocio
- Si hay gasolina suficiente para recorrer todos los kilómetros solicitados:
  - aumenta `kilometros_recorridos`
  - disminuye la gasolina consumida
  - aumenta el acumulado por marca
- Si no hay gasolina suficiente:
  - el coche no avanza
  - no se modifica ningún estado
  - la operación debe informar del error mediante el contrato de resultados definido para el sistema

---

## 3.3 `CocheElectrico`

### Responsabilidad
Representar un coche que utiliza batería.

### Atributos específicos
- `bateria_kwh`: energía disponible, inicializada a `0`

### Consumo
- `0.02` kWh por kilómetro

### Métodos públicos
- `recargar(kwh)`
- `avanzar(km)`

### Reglas de negocio
- Si hay batería suficiente:
  - aumenta `kilometros_recorridos`
  - disminuye la energía consumida
  - aumenta el acumulado por marca
- Si no hay batería suficiente:
  - el coche no avanza
  - no se modifica ningún estado
  - la operación debe informar del error mediante el contrato de resultados definido para el sistema

---

## 3.4 `CocheHibrido`

### Responsabilidad
Representar un coche con batería y gasolina.

### Herencia
Debe heredar de:

- `CocheElectrico`
- `CocheCombustion`

### Regla principal
Debe priorizar el motor eléctrico y **no usar ambos motores a la vez en un mismo recorrido**.

### Política de avance
Para una llamada a `avanzar(km)`:

1. Si la batería permite cubrir **todo** el recorrido, se usa solo el modo eléctrico.
2. Si la batería no alcanza, se intenta cubrir **todo** el recorrido con el motor de combustión.
3. Si ninguna fuente por sí sola cubre el recorrido completo, el coche no avanza.

### Restricción de diseño
La herencia múltiple **no** usará composición parcial interna.
La solución debe resolverse mediante herencia múltiple real y un diseño cuidadoso de métodos comunes y específicos.

### Criterio técnico
Para mantener la duplicación mínima y evitar conflictos innecesarios:

- la lógica compartida debe centralizarse en la jerarquía
- `CocheHibrido` solo resolverá la prioridad entre fuentes de energía
- no debe mezclar consumo de ambas fuentes en una misma llamada a `avanzar(km)`

### Métodos públicos
- `recargar(kwh)`
- `repostar(litros)`
- `avanzar(km)`

---

## 3.5 Clase `Persona`

### Responsabilidad
Representar una persona que puede o no tener un coche.

### Atributos
- `dni`
- `nombre`
- `apellido`
- `coche` (opcional, por defecto `None`)

### Reglas
- Una persona puede tener como máximo un coche.
- El atributo `coche` será opcional al crear la persona.

### Métodos públicos
- `vender_coche(a_persona)`

### Reglas de negocio de `vender_coche`
La operación solo es válida si:

- la persona que vende tiene coche
- la persona que recibe no tiene coche

Si la operación es válida:

- se transfiere la referencia del coche
- quien vende queda sin coche

Si no es válida:

- no se modifica ningún estado
- la operación informa del error mediante el contrato de resultados definido para el sistema

### Representación
- `__str__`
- `__repr__`

---

## 3.6 Clase `Concesionario`

### Responsabilidad
Gestionar inventario de coches y clientes.

### Atributos
- `nombre`
- colección de coches
- colección de clientes

### Comportamientos especiales
- acceso por índice a coches con `[]`
- longitud con `len()`
- evaluación booleana con `__bool__`
  - `True` si hay coches
  - `False` si no hay coches
- `__str__`
- `__repr__`

### Operaciones sobre clientes
- buscar cliente por `DNI`
- añadir cliente
- sustituir cliente
- eliminar cliente

### Reglas de negocio de clientes
- no se puede añadir un cliente con un `DNI` ya existente
- no se puede sustituir un cliente inexistente
- no se puede eliminar un cliente inexistente
- la búsqueda por `DNI` debe devolver el cliente o indicar ausencia

### Operaciones sobre coches
Se permitirá usar los operadores:

- `+`
- `+=`
- `-`
- `-=`

### Semántica obligatoria de operadores
- `+=` muta el objeto actual
- `-=` muta el objeto actual
- `+` devuelve una **copia** del concesionario con el coche añadido
- `-` devuelve una **copia** del concesionario con el coche eliminado
- `concesionario + coche` devuelve un nuevo `Concesionario`
- `concesionario - coche` devuelve un nuevo `Concesionario`

### Reglas de negocio sobre coches
- no se puede añadir un coche duplicado
- no se puede eliminar un coche que no exista
- la identidad del coche se basará en la `matricula`
- cuando una operación no sea válida, se debe informar del error mediante el contrato de resultados definido para el sistema

### Nota de implementación
Aunque `+` y `-` devuelven copia, la semántica de error debe ser coherente con el resto del sistema. Si la operación no es válida, la copia no debe alterar el contenido lógico del concesionario.

---

## 4. Contrato de errores temporal

## 4.1 Objetivo
El sistema no usará todavía excepciones como mecanismo principal de dominio, pero debe quedar preparado para migrar a ellas más adelante.

## 4.2 Regla general
No se permite usar `print()` dentro de `entities` ni dentro de `services`.

Los errores del dominio y de aplicación deben devolverse mediante una clase normal llamada `Resultado`.

## 4.3 Definición
`Resultado` será una clase normal, no un `dataclass`.

Debe permitir representar:

- si la operación tuvo éxito o no
- un mensaje descriptivo
- un código de error opcional
- un valor opcional cuando la operación necesite devolver datos

### Estructura conceptual mínima
- `ok`
- `mensaje`
- `codigo`
- `valor`

### Ejemplo conceptual
Una operación de negocio podrá devolver:

- éxito sin valor
- éxito con valor
- error con mensaje y código

## 4.4 Uso por tipo de operación
- **Comandos** que modifican estado: devuelven `Resultado`
- **Consultas** puras: pueden devolver directamente el objeto buscado o `None`

## 4.5 Beneficio
Este contrato permite una migración posterior a excepciones con cambios reducidos en UI y servicios.

---

## 5. Identidad y representación

## 5.1 Identidad de negocio
- coche: `matricula`
- persona: `dni`

## 5.2 `__repr__`
`__repr__` será válido para reconstrucción de objetos.

### Regla
Debe devolver una cadena con formato técnico y suficiente información para recrear el objeto de forma razonable.

## 5.3 `__str__`
`__str__` será legible y orientado a personas usuarias.

---

## 6. Arquitectura por capas

La arquitectura del proyecto se organizará en estas carpetas:

- `entities`
- `persistence`
- `services`
- `ui`

La solución debe priorizar:
- simplicidad
- encapsulación
- bajo acoplamiento
- alta cohesión
- duplicación mínima
- separación clara de responsabilidades

Restricciones: 
- Mantén las carpetas: `entities/`, `services/`, `persistence/`, `ui/` y `main.py` en raíz.
- Direcciones de dependencia: `ui -> services -> entities`.
- `persistence/` debe existir desde la primera versión, aunque quede mínima.
- No pongas I/O de consola, persistencia ni `print()` dentro de `entities/` o `services/`.

Orden recomendado de implementación:
- 1) Implementa primero `entities/` y valida invariantes de dominio.
- 2) Añade `services/` solo para orquestación de casos de uso.
- 3) Crea `ui/menu.py` como CLI delgada (traducción entrada/salida).
- 4) Deja `persistence/__init__.py` preparado para evolución futura.
- 5) Conecta arranque e inyección básica en `main.py`.

  
Además:
- no se aplicará TDD
- no se aplicará BDD
- se permite el uso de clases abstractas
- los `type hints` se consideran una mejora futura
- se seguirá la norma de estilo **PEP 8**


## 6.1 Regla general para decidir entre `entities` y `services`

Esta será la regla principal:

### La lógica va en `entities` si:
- protege invariantes del objeto
- modifica el estado interno de una entidad concreta
- pertenece claramente al significado del objeto en el dominio
- puede ejecutarse sin conocer repositorios, almacenamiento ni flujo de aplicación

### La lógica va en `services` si:
- coordina varias entidades
- organiza un caso de uso completo
- necesita decidir el orden de varias operaciones
- depende de colaboración entre objetos que no deberían conocerse directamente
- en el futuro dependerá de persistencia, repositorios o transacciones

### Regla práctica resumida
- **Comportamiento propio del objeto** -> `entities`
- **Orquestación del caso de uso** -> `services`

Esta es la regla más adecuada porque mantiene un dominio rico sin convertir los servicios en un contenedor de toda la lógica.

---

## 6.2 `entities`

### Qué contiene
Las clases del dominio y sus reglas de negocio puras:

- `coche.py`
- `coche_combustion.py`
- `coche_electrico.py`
- `coche_hibrido.py`
- `persona.py`
- `concesionario.py`
- `resultado.py`

### Responsabilidades
- modelar entidades del negocio
- validar invariantes del dominio
- encapsular estado
- implementar comportamiento propio del dominio
- mantener `__str__`, `__repr__`, propiedades y operadores
- devolver `Resultado` cuando una operación modificadora pueda fallar

### Qué no debe contener
- lectura por teclado
- impresión por consola
- persistencia en archivo o base de datos
- menús
- lógica de aplicación ajena al objeto

---

## 6.3 `persistence`

### Situación actual
Por ahora la persistencia es **en memoria**, por lo que esta capa queda vacía en la primera versión.

### Regla de diseño
La carpeta debe existir desde el principio para reservar la responsabilidad arquitectónica, aunque inicialmente no contenga implementación relevante.

### Evolución futura prevista
Más adelante esta capa podrá incorporar:

- persistencia en ficheros
- persistencia en base de datos

### Responsabilidades futuras
- guardar y recuperar datos
- aislar detalles de almacenamiento
- evitar que `entities` y `services` dependan del formato de persistencia

### Qué no debe contener
- reglas de negocio del dominio
- interacción con consola

---

## 6.4 `services`

### Qué contiene
Casos de uso y coordinación entre entidades.

### Responsabilidades
- orquestar operaciones del sistema
- coordinar varias entidades cuando el flujo no pertenezca a una sola
- preparar el diseño para futura integración con persistencia real
- devolver resultados listos para la UI

### Ejemplos de casos de uso apropiados
- transferir un coche localizando personas por DNI
- alta de cliente a partir de datos de entrada
- baja de cliente
- incorporación de coche al inventario a través del flujo de aplicación
- consultas agregadas del sistema

### Qué no debe contener
- lógica de bajo nivel de persistencia
- impresión o lectura de consola
- lógica interna que ya pertenece claramente a una entidad

---

## 6.5 `ui`

### Qué contiene
La interfaz de usuario más simple posible.

### Decisión de simplicidad
La UI será una **CLI**.

### Posibles módulos
- `menu.py`

### Responsabilidades
- mostrar menús
- pedir datos al usuario
- invocar solo servicios (nunca entidades directamente)
- mostrar resultados y errores

### Qué no debe contener
- lógica de negocio
- persistencia
- cambios directos de estado saltándose las reglas del dominio
- imports directos desde `entities/` (la dependencia obligatoria es `ui -> services`)

---

## 6.6 Punto de entrada

El archivo `main.py` estará en el directorio raíz del proyecto y no dentro de `ui`.

### Responsabilidad de `main.py`
- arrancar la aplicación
- crear dependencias
- instanciar los objetos principales
- delegar la interacción a la UI

---

## 7. Estructura recomendada del proyecto

    proyecto/
    ├── entities/
    │   ├── coche.py
    │   ├── coche_combustion.py
    │   ├── coche_electrico.py
    │   ├── coche_hibrido.py
    │   ├── persona.py
    │   ├── concesionario.py
    │   └── resultado.py
    ├── persistence/
    │   └── __init__.py
    ├── services/
    │   ├── __init__.py
    │   ├── gestion_concesionario_service.py
    │   └── gestion_personas_service.py
    ├── ui/
    │   ├── __init__.py
    │   └── menu.py
    ├── main.py
    └── README.md

---

## 8. Principios de implementación

## 8.1 Simplicidad primero
La solución debe evitar patrones innecesarios y estructuras artificiales.

## 8.2 Responsabilidad única
Cada clase y cada carpeta deben tener una responsabilidad clara.

## 8.3 Dominio independiente
Las entidades no deben depender de UI ni de persistencia.

## 8.4 Validación antes de mutar
Toda operación debe validar primero y modificar el estado solo si es válida.

## 8.5 Estado consistente
Ante error:

- no se actualizan kilómetros
- no se descuentan energías
- no se alteran clientes o coches parcialmente

## 8.6 Duplicación mínima
Se debe reutilizar lógica común siempre que no aumente innecesariamente el acoplamiento ni complique el diseño.

## 8.7 Estilo
El código debe seguir **PEP 8**.

## 8.8 Encapsulación, visibilidad y propiedades

### Motivación de diseño OO
Estas reglas se apoyan en principios clásicos de diseño orientado a objetos:
- **Encapsulación** e **information hiding**: proteger invariantes internas.
- **Principio de menor privilegio**: exponer solo lo necesario.
- **Alta cohesión y bajo acoplamiento**: minimizar dependencias externas al estado interno.

### Criterio de visibilidad en este proyecto
- **Público**: solo operaciones del contrato de dominio o de consulta necesarias para otros objetos/capas.
- **Protegido** (`_`): helpers internos de jerarquía y puntos de extensión entre clases relacionadas.
- **Privado** (`__`): estado interno que no debe manipularse desde fuera de la clase.

### Cuándo añadir propiedades (`@property`)
- Usar propiedades de lectura para exponer datos de entidad sin abrir mutación directa.
- Si un atributo forma parte de la identidad o de una invariante, priorizar lectura mediante propiedad y mutación por métodos de dominio.
- Evitar propiedades para lógica compleja o con efectos secundarios.

### Cuándo añadir setters
- En `entities`, **no** añadir setters públicos por defecto.
- Añadir setter solo si existe una necesidad real del dominio y el setter valida invariantes antes de mutar.
- Si la mutación implica reglas de negocio, preferir métodos explícitos (`avanzar`, `repostar`, `vender_coche`) en lugar de setters genéricos.
- En caso de duda: propiedad de solo lectura + método de dominio con validación.

---

## 9. Decisiones de modelado cerradas

1. `Resultado` será una clase normal.
2. `Coche` será abstracta.
3. Se prioriza duplicación mínima.
4. `CocheHibrido` usará herencia múltiple real, sin composición parcial interna.
5. `+=` y `-=` mutan el concesionario actual.
6. `+` y `-` devuelven copia.
7. `main.py` estará en la raíz del proyecto.
8. La persistencia está vacía en la primera versión, pero la carpeta existe para evolución futura.
9. `__repr__` será válido para reconstrucción de objetos.
10. Los `type hints` se dejan como mejora futura.
11. Se aplicará PEP 8.
12. La visibilidad y mutación se rigen por encapsulación: estado interno privado, API mínima pública y setters solo con validación de invariantes.

---

## 10. Criterios de aceptación del producto

1. Debe ser posible crear personas con o sin coche.
2. Debe ser posible crear coches de combustión, eléctricos e híbridos.
3. Los coches deben acumular kilómetros individuales y por marca.
4. Un coche de combustión no debe avanzar sin gasolina suficiente.
5. Un coche eléctrico no debe avanzar sin batería suficiente.
6. Un coche híbrido debe priorizar batería y usar una sola fuente por recorrido.
7. Una persona solo puede tener un coche a la vez.
8. La venta de coche entre personas debe respetar las validaciones del dominio.
9. El concesionario debe gestionar clientes por DNI.
10. El concesionario debe permitir añadir y quitar coches con operadores.
11. `+` y `-` deben devolver un nuevo concesionario.
12. `+=` y `-=` deben mutar el concesionario actual.
13. El código debe estar separado en `entities`, `persistence`, `services` y `ui`.
14. La UI no debe contener lógica de negocio.
15. La persistencia no debe contener reglas del dominio.
16. Las entidades no deben depender de la consola ni del almacenamiento.
17. Los errores no deben comunicarse con `print()` desde dominio o servicios.
18. El contrato de error temporal debe basarse en `Resultado`.
19. El código debe seguir PEP 8.
20. `__repr__` debe ser técnico y útil para reconstrucción.

---

## 11. Resumen ejecutivo

Esta aplicación de gestión de coches, personas y concesionarios tiene las siguientes características: 
- dominio bien encapsulado
- herencia y polimorfismo donde aportan valor real
- duplicación mínima
- separación clara entre entidades, servicios, persistencia futura e interfaz
- contrato uniforme de errores mediante una clase `Resultado`
- herencia múltiple real en `CocheHibrido`
- punto de entrada en la raíz del proyecto
- estilo PEP 8
- persistencia preparada para evolucionar a ficheros y base de datos

La aplicación está preparada para evolucionar hacia persistencia en base de datos, ficheros, etc. después sin rehacer el diseño principal.