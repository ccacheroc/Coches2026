---
applyTo: '**/*.py'
description: 'Reglas de arquitectura por capas del proyecto Coches2026'
---

# Arquitectura por capas — Coches2026

## Capas y responsabilidades

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| Dominio | `entities/` | Entidades, invariantes, reglas de negocio, `Resultado` |
| Servicios | `services/` | Orquestación de casos de uso; no hay I/O de consola |
| Interfaz | `ui/` | Entrada/salida de consola, menús, traducción de `Resultado` a mensajes |
| Persistencia | `persistence/` | Reservado para almacenamiento futuro |

## Regla de dependencias (unidireccional)

```
ui  →  services  →  entities
                ↘  persistence  (futuro)
```

- `ui` **solo** importa de `services`. Prohibido `from entities import ...` en `ui/`.
- `services` importa de `entities` y (en el futuro) de `persistence`.
- `entities` no importa de ninguna otra capa del proyecto.

## Contrato de errores: `Resultado`

Todas las operaciones que pueden fallar **deben** devolver `Resultado` en lugar de lanzar excepciones al exterior.

```python
# ✅ Correcto
def avanzar(self, km: float) -> Resultado:
    if km <= 0:
        return Resultado.error("Los km deben ser positivos", "KM_INVALIDOS")
    ...
    return Resultado.exito(f"Avanzado {km} km")

# ❌ Incorrecto — lanzar excepción desde dominio hacia servicios/ui
def avanzar(self, km: float) -> None:
    raise ValueError("km inválidos")
```

## Seed de datos

`services/seed_data_service.py` inserta datos de ejemplo al arrancar.
Se invoca desde `main.py` **antes** de lanzar el menú.
Las entidades desconocen que son "datos de seed".

## Añadir nueva funcionalidad — checklist

1. Invariante → `entities/` (sin I/O).
2. Caso de uso → `services/` (método en el servicio adecuado).
3. Pantalla/menú → `ui/menu.py` (llama al servicio, muestra `Resultado.mensaje`).
4. Test → `tests/test_<capa>.py` con Given/When/Then.

