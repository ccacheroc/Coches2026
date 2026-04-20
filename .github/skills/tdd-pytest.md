# Skill: Escribir tests con pytest en Coches2026

## Cuándo usar esta skill

Cárgala cuando debas escribir, revisar o ampliar tests del proyecto.

---

## Estructura obligatoria de cada test

```python
def test_descripcion_corta_de_lo_que_se_prueba():
    # Given — estado inicial / contexto
    coche = CocheCombustion("1234ABC", "Seat")
    coche.repostar(10.0)

    # When — acción que se prueba
    resultado = coche.avanzar(50)

    # Then — verificación del resultado esperado
    assert resultado.ok is True
    assert coche.kilometros_recorridos == 50.0
```

---

## Dónde va cada tipo de test

| Qué se prueba | Fichero |
|---|---|
| Entidades y reglas de negocio | `tests/test_entities.py` |
| `GestionConcesionarioService` | `tests/test_gestion_concesionario_service.py` |
| `GestionPersonasService` | `tests/test_gestion_personas_service.py` |
| `SeedDataService` | `tests/test_seed_data_service.py` |
| Menú / UI | `tests/test_ui_menu.py` |

---

## Reglas de este proyecto

1. **Tests de entidades**: sin mocks. Instanciar directamente la clase y verificar comportamiento.
2. **Tests de servicios**: usar mocks (`unittest.mock.MagicMock`) para sustituir dependencias externas si las hubiera.
3. **Tests de UI**: mockear los servicios; nunca instanciar entidades en tests de `ui/`.
4. **Nombrar el test** con el patrón: `test_<clase_o_función>_<escenario>`.
   - Ejemplo: `test_coche_combustion_avanzar_sin_gasolina_devuelve_error`.
5. **Cubrir al menos** tres escenarios por funcionalidad: happy path, error de dominio, y edge case (valor límite).

---

## Ejecutar los tests

```bash
# Todos los tests
python -m pytest -q

# Solo un fichero
python -m pytest tests/test_entities.py -v

# Solo tests que contienen una palabra
python -m pytest -k "avanzar" -v
```

---

## Ejemplo de test de error de dominio

```python
def test_coche_combustion_avanzar_sin_gasolina_devuelve_error():
    # Given
    coche = CocheCombustion("9999ZZZ", "Ford")
    # sin repostar → gasolina = 0

    # When
    resultado = coche.avanzar(100)

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "SIN_COMBUSTIBLE"
```

---

## Ejemplo de test de UI (mock de servicio)

```python
from unittest.mock import MagicMock, patch

def test_menu_muestra_error_cuando_servicio_falla():
    # Given
    servicio_mock = MagicMock()
    servicio_mock.dar_de_alta_cliente.return_value = Resultado.error("DNI duplicado", "DNI_DUPLICADO")

    menu = MenuCLI(servicio_mock, servicio_mock)

    # When / Then — se verifica que el menú imprime el mensaje de error
    with patch("builtins.input", side_effect=["1", "1", "12345678A", "Ana", "García", "0"]):
        with patch("builtins.print") as mock_print:
            menu.iniciar()
            mensajes = [str(c) for c in mock_print.call_args_list]
            assert any("DNI duplicado" in m for m in mensajes)
```

