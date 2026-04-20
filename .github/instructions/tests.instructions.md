---
applyTo: 'tests/**/*.py'
description: 'Reglas específicas para la capa de tests (tests/)'
---

# Reglas — Capa `tests/`

## Responsabilidad

Los tests validan el comportamiento del sistema capa por capa.
Cada fichero de test corresponde a un módulo concreto del proyecto.

## Estructura de ficheros

| Fichero | Qué prueba |
|---|---|
| `tests/test_entities.py` | Entidades y reglas de negocio (sin mocks) |
| `tests/test_gestion_concesionario_service.py` | `GestionConcesionarioService` |
| `tests/test_gestion_personas_service.py` | `GestionPersonasService` |
| `tests/test_seed_data_service.py` | `SeedDataService` |
| `tests/test_ui_menu.py` | `MenuCLI` (con servicios mockeados) |

## Estructura obligatoria de cada test

```python
def test_nombre_descriptivo_del_escenario():
    # Given — estado inicial / contexto
    coche = CocheCombustion("1234ABC", "Seat")
    coche.repostar(10.0)

    # When — acción bajo prueba
    resultado = coche.avanzar(50)

    # Then — verificaciones
    assert resultado.ok is True
    assert coche.kilometros_recorridos == 50.0
```

## Reglas por tipo de test

### Tests de entidades (`test_entities.py`)
- **Sin mocks**. Instanciar directamente la clase y verificar comportamiento.
- Cubrir: happy path + error de dominio + edge case (valor límite 0, negativo, etc.).

### Tests de servicios
- Mockear dependencias externas si las hubiera (repositorios de persistencia).
- No mockear entidades — usar instancias reales.

### Tests de UI (`test_ui_menu.py`)
- Mockear los servicios con `unittest.mock.MagicMock`.
- **Prohibido** importar o instanciar entidades aquí.
- Usar `patch("builtins.input", side_effect=[...])` para simular entradas del usuario.

```python
from unittest.mock import MagicMock, patch
from entities.resultado import Resultado
from ui.menu import MenuCLI

def test_menu_alta_cliente_exitosa():
    # Given
    gp_mock = MagicMock()
    gp_mock.dar_de_alta_cliente.return_value = Resultado.exito("Cliente registrado")
    gc_mock = MagicMock()
    menu = MenuCLI(gc_mock, gp_mock)

    # When / Then
    with patch("builtins.input", side_effect=["1", "1", "12345678A", "Ana", "García", "", "0", "0"]):
        with patch("builtins.print") as mock_print:
            menu.iniciar()
            salidas = " ".join(str(c) for c in mock_print.call_args_list)
            assert "Cliente registrado" in salidas
```

## Ejecución

```bash
python -m pytest -q                      # todos los tests
python -m pytest tests/test_entities.py -v   # solo entidades
python -m pytest -k "avanzar" -v         # filtrar por nombre
```

## Nombrado de tests

Patrón: `test_<clase_o_función>_<escenario_en_snake_case>`

```
test_coche_combustion_avanzar_sin_gasolina_devuelve_error
test_concesionario_anadir_cliente_dni_duplicado_devuelve_error
test_menu_listar_coches_llama_al_servicio
```

