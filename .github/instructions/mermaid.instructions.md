---
applyTo: 'README.md'
description: 'Reglas para generar diagramas Mermaid (UML de clases y C4) en este proyecto'
---

# Reglas — Diagramas Mermaid en Coches2026

Se activa automáticamente al editar `README.md`.
Aplica tanto al diagrama UML de clases como al diagrama C4 de arquitectura.

---

## Diagrama UML de clases (`classDiagram`)

### Plantilla base

```mermaid
classDiagram
    class NombreClase {
        <<abstract>>
        -tipo __atributo_privado
        #tipo _atributo_protegido
        +tipo atributo_publico
        +metodo(param: tipo) TipoRetorno
    }
```

### Reglas específicas para Coches2026

1. **Visibilidad**: `-` para `__privado`, `#` para `_protegido`, `+` para público/property.
2. **Propiedades**: mostrarlas como atributos `+` sin paréntesis — son la interfaz observable.
3. **`Resultado`**: incluirlo siempre como clase separada con sus métodos `exito` y `error`.
4. **Herencia**: `Padre <|-- Hijo` (la flecha apunta al padre).
5. **Agregación/composición**: `o--` para agregación débil, `*--` para composición fuerte.
6. **Dependencias de retorno**: `..>` para indicar que una clase usa `Resultado`.
7. **Servicios y UI**: incluirlos sin atributos (solo nombre de clase) para mostrar la arquitectura completa.

### Ejemplo correcto

```mermaid
classDiagram
    class Coche {
        <<abstract>>
        -str __matricula
        -str __marca
        -float __kilometros_recorridos
        +matricula str
        +marca str
        +kilometros_recorridos float
        +avanzar(km: float) Resultado
        +obtener_km_por_marca(marca: str) float
    }
    class CocheCombustion {
        -float __gasolina
        +gasolina float
        +repostar(litros: float) Resultado
    }
    class CocheElectrico {
        -float __bateria_kwh
        +bateria_kwh float
        +recargar(kwh: float) Resultado
    }
    class CocheHibrido {
        +avanzar(km: float) Resultado
    }
    class Resultado {
        +bool ok
        +str mensaje
        +str codigo
        +any valor
        +exito(mensaje, valor)$
        +error(mensaje, codigo, valor)$
    }

    Coche <|-- CocheCombustion
    Coche <|-- CocheElectrico
    CocheCombustion <|-- CocheHibrido
    CocheElectrico <|-- CocheHibrido
    Coche ..> Resultado
```

### Errores comunes a evitar

- ❌ `+matricula()` con paréntesis en una property → ✅ `+matricula str`
- ❌ Omitir `<<abstract>>` en `Coche`
- ❌ No incluir `Resultado` como clase propia
- ❌ Mezclar inglés y español en nombres de elementos

---

## Diagrama C4 de arquitectura (`C4Container`)

### Niveles relevantes para este proyecto

- **Nivel 2 – Contenedores**: las cuatro capas. **Este es el nivel habitual.**
- **Nivel 3 – Componentes**: solo si se detalla una capa concreta.

### Plantilla Nivel 2

```mermaid
C4Container
    title Arquitectura C4 (nivel contenedor) — Coches2026

    Person(usuario, "Usuario", "Opera la app por CLI")

    Container_Boundary(sistema, "Coches2026") {
        Container(ui, "UI CLI", "Python / ui/", "Entrada/salida de consola y menús")
        Container(servicios, "Services", "Python / services/", "Orquesta casos de uso")
        Container(dominio, "Entities", "Python / entities/", "Reglas de negocio y modelo de dominio")
        Container(persistencia, "Persistence", "Python / persistence/", "Almacenamiento futuro")
    }

    Rel(usuario, ui, "Usa")
    Rel(ui, servicios, "Invoca casos de uso")
    Rel(servicios, dominio, "Manipula entidades")
    Rel(servicios, persistencia, "Guardará datos", "(futuro)")
```

### Reglas para este proyecto

1. **Nunca** dibujar flecha `ui → dominio`; viola la arquitectura.
2. `persistence` aparece siempre aunque esté vacía — comunica la intención arquitectónica.
3. Usar `Container_Boundary` para agrupar todas las capas dentro del sistema.

### Errores comunes a evitar

- ❌ Usar `graph TD` en lugar de `C4Container`
- ❌ Omitir `persistence` del diagrama porque está vacía

