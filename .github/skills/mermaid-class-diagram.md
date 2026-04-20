# Skill: Generar diagrama de clases UML en Mermaid

## Cuándo usar esta skill

Cárgala cuando debas generar o actualizar el diagrama de clases en `README.md` o en cualquier documento del proyecto.

---

## Plantilla base para este proyecto

````mermaid
classDiagram
    class NombreClase {
        <<abstract>>            %% solo si es abstracta
        -tipo __atributo_privado
        #tipo _atributo_protegido
        +tipo atributo_publico
        +metodo(param: tipo) TipoRetorno
    }
````

## Reglas específicas para Coches2026

1. **Visibilidad**: usar `-` para `__privado`, `#` para `_protegido`, `+` para público/property.
2. **Propiedades**: mostrarlas como atributos `+` (sin paréntesis), ya que son la interfaz observable.
3. **Resultado**: incluirlo siempre como clase separada con sus métodos `exito` y `error`.
4. **Relaciones de herencia**: `Padre <|-- Hijo` (la flecha apunta al padre).
5. **Composición/agregación**: usar `o--` para agregación débil (el hijo puede existir sin el padre), `*--` para composición fuerte.
6. **Dependencias**: usar `..>` para indicar que una clase usa `Resultado` como valor de retorno.
7. **Capas de servicios y UI**: incluirlas sin atributos (solo nombre) para mostrar la arquitectura.

## Ejemplo correcto para este proyecto

````mermaid
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
        +repostar_gasolina(litros: float) Resultado
        +recargar_bateria(kwh: float) Resultado
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
````

## Errores comunes a evitar

- ❌ No usar `Optional[X]` en los tipos — Mermaid no lo renderiza bien. Usar `X|None`.
- ❌ No poner paréntesis vacíos en propiedades: `+matricula()` → ✅ `+matricula str`.
- ❌ No omitir `<<abstract>>` en `Coche`.
- ❌ No mezclar inglés y español en los nombres de los elementos del diagrama.

