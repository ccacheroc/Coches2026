from entities.coche import Coche
from entities.coche_combustion import CocheCombustion
from entities.coche_electrico import CocheElectrico
from entities.coche_hibrido import CocheHibrido
from entities.concesionario import Concesionario
from entities.persona import Persona


def test_coche_combustion_avanza_si_hay_gasolina():
    # Given
    coche = CocheCombustion("1111AAA", "Seat")
    coche.repostar(10)

    # When
    resultado = coche.avanzar(100)

    # Then
    assert resultado.ok is True
    assert coche.kilometros_recorridos == 100
    assert round(coche.gasolina, 2) == 5.0


def test_coche_electrico_no_avanza_sin_bateria():
    # Given
    coche = CocheElectrico("2222BBB", "Tesla")

    # When
    resultado = coche.avanzar(10)

    # Then
    assert resultado.ok is False
    assert coche.kilometros_recorridos == 0


def test_coche_hibrido_prioriza_bateria():
    # Given
    coche = CocheHibrido("3333CCC", "Toyota")
    coche.recargar(1)
    coche.repostar(50)

    # When
    resultado = coche.avanzar(10)

    # Then
    assert resultado.ok is True
    assert resultado.valor == "electrico"
    assert round(coche.bateria_kwh, 2) == 0.8
    assert coche.gasolina == 50


def test_venta_coche_valida():
    # Given
    vendedor = Persona("1", "Ana", "Lopez", CocheCombustion("4444DDD", "Ford"))
    comprador = Persona("2", "Luis", "Perez")

    # When
    resultado = vendedor.vender_coche(comprador)

    # Then
    assert resultado.ok is True
    assert vendedor.coche is None
    assert comprador.coche is not None


def test_concesionario_operadores_copia_y_mutacion():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("5555EEE", "Seat")

    # When
    copia = concesionario + coche

    # Then
    assert len(concesionario) == 0
    assert len(copia) == 1

    # When
    concesionario += coche

    # Then
    assert len(concesionario) == 1


def test_kilometros_por_marca_acumula():
    # Given
    marca = "MarcaTest"
    c1 = CocheCombustion("6666FFF", marca)
    c2 = CocheElectrico("7777GGG", marca)
    c1.repostar(10)
    c2.recargar(10)

    # When
    c1.avanzar(20)
    c2.avanzar(30)

    # Then
    total = Coche.obtener_kilometros_por_marca(marca)
    assert round(total, 2) >= 50.0

