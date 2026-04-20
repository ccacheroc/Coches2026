---
applyTo: 'entities/**/*.py'
description: 'Reglas específicas para la capa de dominio (entities/): arquitectura, visibilidad, properties y setters'
---

# Reglas — Capa `entities/`

## Responsabilidad

Esta capa contiene el **modelo de dominio puro**: entidades, invariantes y reglas de negocio.
No tiene dependencias con ninguna otra capa del proyecto.

## Prohibiciones absolutas

- ❌ `print()`, `input()` o cualquier I/O de consola.
- ❌ Acceso a ficheros, red o base de datos.
- ❌ Importar desde `services/`, `ui/` o `persistence/`.
- ❌ Atributos de instancia públicos sin pasar por `@property`.

---

## Diseño OO — Visibilidad, Properties y Setters

### Principio fundamental

> **Ocultar la implementación, exponer el comportamiento.**
> (Principio de encapsulación — Parnas, 1972; reforzado en "Clean Code" y "SOLID".)

Un atributo nunca debe ser público por comodidad. Debe ser público solo si forma parte intencional de la interfaz de la clase.

### `__doble_guion` → Privado (name-mangling)

Usar cuando:
- El atributo es un **detalle de implementación** que no debe ser accedido ni sobrescrito por subclases.
- Su modificación directa rompería invariantes del objeto.
- Es la opción **por defecto** en `entities/`.

```python
class Coche(ABC):
    def __init__(self, matricula: str, marca: str) -> None:
        if not matricula:
            raise ValueError("La matrícula no puede estar vacía")
        self.__matricula: str = matricula        # ← privado
        self.__kilometros_recorridos: float = 0.0  # ← privado
```

### `_un_guion` → Protegido (convención)

Usar **solo** cuando una subclase necesita leerlo o modificarlo directamente y añadir una `@property` sería artificialmente verboso.
Documentar siempre el motivo.

```python
class CocheCombustion(Coche):
    def __init__(self, ...) -> None:
        self._gasolina: float = 0.0  # accesible por CocheHibrido
```

### Sin guion → Público

Usar únicamente para:
- Constantes de clase que son parte de la API pública.
- Atributos de objetos de datos simples (ej. `Resultado`) donde la transparencia es deliberada.

### Cuándo añadir `@property` (lectura)

Añadir `@property` cuando:
1. El atributo forma parte de la **interfaz observable** de la entidad (ej. `matricula`, `kilometros_recorridos`).
2. Otra capa (`services`, `ui`) necesita leerlo para mostrar información.
3. Podría requerir lógica en el futuro (cálculo derivado, logging, lazy init).

```python
@property
def matricula(self) -> str:
    """Matrícula del coche (solo lectura)."""
    return self.__matricula
```

**No añadir `@property`** si el atributo es un detalle interno que nunca sale de la clase.

### Cuándo añadir setter (`@xxx.setter`)

Añadir setter **solo** si se cumplen **las dos** condiciones:
1. La mutación es parte explícita del **dominio** (ej. asignar un coche a una persona).
2. Hay **lógica de validación** que debe ejecutarse al asignar.

```python
@coche.setter
def coche(self, nuevo_coche: "Coche | None") -> None:
    """Asigna un coche a la persona; None indica que no tiene coche."""
    # la validación de negocio vive en Persona.vender_coche(), no aquí
    self.__coche = nuevo_coche
```

**No añadir setter** si:
- El valor se establece solo en `__init__` y no cambia (ej. `matricula`).
- La mutación se hace a través de un método de dominio con nombre explícito (preferir `transferir_coche()` sobre un setter genérico).

### Resumen rápido de visibilidad

| Situación | Solución |
|---|---|
| Atributo interno, no sale de la clase | `self.__atributo` (privado, sin property) |
| Atributo que services/ui necesita leer | `self.__atributo` + `@property` de lectura |
| Atributo mutable con validación de dominio | `self.__atributo` + `@property` + `@xxx.setter` |
| Subclase necesita acceso directo | `self._atributo` (protegido, documentar motivo) |
| API pública deliberada / constante | sin guion |

---

## Contrato de errores

Toda operación que puede fallar por **lógica de negocio** devuelve `Resultado`:

```python
def avanzar(self, km: float) -> Resultado:
    if km <= 0:
        return Resultado.error("Los km deben ser positivos", "KM_INVALIDOS")
    ...
    return Resultado.exito(f"Avanzado {km} km")
```

Las excepciones (`ValueError`, clases propias de `excepciones.py`) se reservan para **invariantes de construcción** (datos de entrada inválidos que son un bug del llamador).

---

## Atributos de clase

Usar `ClassVar` y documentar su propósito:

```python
from typing import ClassVar

class Coche(ABC):
    __km_por_marca: ClassVar[dict[str, float]] = {}
```

## Type hints

Obligatorios en todas las firmas públicas. Usar `X | None` (nunca `Optional[X]`).

## Clases abstractas

`Coche` es abstracta (`ABC`). Decorar con `@abstractmethod` los métodos que cada subclase debe implementar obligatoriamente (`avanzar`).

## Herencia múltiple

`CocheHibrido` hereda de `CocheElectrico` y `CocheCombustion`.
Documentar el MRO elegido con un comentario en la clase:

```python
# MRO: CocheHibrido → CocheElectrico → CocheCombustion → Coche
class CocheHibrido(CocheElectrico, CocheCombustion):
    ...
```
