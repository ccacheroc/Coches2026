---
applyTo: 'ui/**/*.py'
description: 'Reglas específicas para la capa de interfaz de usuario (ui/)'
---

# Reglas — Capa `ui/`

## Responsabilidad

Esta capa es la **única** que interactúa con el usuario: recibe entradas por consola y muestra resultados.
Traduce las acciones del usuario en llamadas a `services/` y convierte `Resultado` en mensajes legibles.

## Dependencias permitidas

- ✅ Importar desde `services/`.
- ❌ **Prohibido importar desde `entities/`** — ni clases, ni tipos, ni constantes.
- ❌ No instanciar entidades directamente (`Coche(...)`, `Persona(...)`, etc.).

## Patrón de llamada a servicios

```python
# ✅ Correcto: la UI llama al servicio y muestra el mensaje de Resultado
resultado = self.__servicio.registrar_coche(matricula, marca, tipo)
if resultado.ok:
    print(f"✅ {resultado.mensaje}")
else:
    print(f"❌ {resultado.mensaje}")

# ❌ Incorrecto: la UI instancia entidades directamente
from entities.coche_combustion import CocheCombustion   # PROHIBIDO
coche = CocheCombustion(matricula, marca)
```

## Estructura del menú (`ui/menu.py`)

- Clase `MenuCLI` con inyección de dependencias de servicios en `__init__`.
- Método `iniciar()` como punto de entrada del bucle principal.
- Cada opción de menú tiene su propio método privado (`__alta_cliente`, `__listar_coches`, etc.).
- Usar `try/except` solo para capturar excepciones de construcción que los servicios no hayan podido interceptar.

```python
class MenuCLI:
    def __init__(
        self,
        gestion_concesionario: GestionConcesionarioService,
        gestion_personas: GestionPersonasService,
    ) -> None:
        self.__gc = gestion_concesionario
        self.__gp = gestion_personas

    def iniciar(self) -> None:
        """Arranca el bucle principal del menú."""
        ...
```

## Entrada de datos

- Validar formato básico en la UI (campo vacío, tipo de dato).
- Validar **lógica de negocio** en `entities/` o `services/`, nunca en `ui/`.
- Usar `input().strip()` siempre para evitar espacios accidentales.

## Mostrar objetos

Llamar siempre a `str(objeto)` o `resultado.mensaje`.
No acceder a propiedades internas de las entidades directamente desde `ui/`.

