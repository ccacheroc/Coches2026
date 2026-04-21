from src.entities.coche_combustion import CocheCombustion
from src.entities.coche_electrico import CocheElectrico
from src.entities.coche_hibrido import CocheHibrido
from src.entities.concesionario import Concesionario
from src.entities.persona import Persona
from src.services.gestion_concesionario_service import GestionConcesionarioService


def test_alta_coche_crea_e_incorpora():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)

    # When
    resultado = service.alta_coche("combustion", "1111AAA", "Seat")

    # Then
    assert resultado.ok is True
    assert len(concesionario) == 1


def test_baja_coche_por_matricula_falla_si_asociado():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)
    concesionario.anadir_cliente(Persona("1", "Ana", "Lopez", coche))
    service = GestionConcesionarioService(concesionario)

    # When
    resultado = service.baja_coche_por_matricula("1111AAA")

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "COCHE_ASOCIADO"


def test_modificar_coche_actualiza_marca():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)
    service = GestionConcesionarioService(concesionario)

    # When
    resultado = service.modificar_coche("1111AAA", "Cupra")

    # Then
    assert resultado.ok is True
    assert concesionario[0].marca == "Cupra"


def test_listar_coches_con_cliente_indica_dni_o_libre():
    # Given
    concesionario = Concesionario("Demo")
    coche_libre = CocheCombustion("1111AAA", "Seat")
    coche_con_duenio = CocheCombustion("2222BBB", "Ford")
    concesionario.agregar_coche(coche_libre)
    concesionario.agregar_coche(coche_con_duenio)
    concesionario.anadir_cliente(Persona("10", "Luis", "Perez", coche_con_duenio))
    service = GestionConcesionarioService(concesionario)

    # When
    coches = service.listar_coches_con_cliente()

    # Then
    por_matricula = {coche["matricula"]: coche for coche in coches}
    assert por_matricula["1111AAA"]["dni_propietario"] is None
    assert por_matricula["2222BBB"]["dni_propietario"] == "10"


def test_listar_kilometros_por_marca_devuelve_acumulados():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)
    marca = "MarcaKmService"

    c1 = CocheCombustion("7777HHH", marca)
    c2 = CocheElectrico("8888III", marca)
    c1.repostar(10)
    c2.recargar(10)
    c1.avanzar(20)
    c2.avanzar(30)

    # When
    filas = service.listar_kilometros_por_marca()

    # Then
    por_marca = {fila["marca"]: fila["kilometros"] for fila in filas}
    assert marca in por_marca
    assert por_marca[marca] >= 50.0


def test_avanzar_coche_por_matricula_happy_path():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)
    coche = CocheCombustion("9999ZZZ", "Seat")
    coche.repostar(10)
    concesionario.agregar_coche(coche)

    # When
    resultado = service.avanzar_coche_por_matricula("9999ZZZ", 50)

    # Then
    assert resultado.ok is True
    assert coche.kilometros_recorridos == 50


def test_cargar_energia_coche_hibrido_pide_litros_y_kwh():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)
    coche = CocheHibrido("8888YYY", "Toyota")
    concesionario.agregar_coche(coche)

    # When
    resultado = service.cargar_energia_coche_por_matricula("8888YYY", litros=5, kwh=3)

    # Then
    assert resultado.ok is True
    assert coche.gasolina == 5.0
    assert coche.bateria_kwh == 3.0


def test_obtener_tipo_coche_por_matricula():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)
    coche = CocheCombustion("3333PPP", "Seat")
    concesionario.agregar_coche(coche)

    # When
    resultado = service.obtener_tipo_coche_por_matricula("3333PPP")

    # Then
    assert resultado.ok is True
    assert resultado.valor == "CocheCombustion"


def test_avanzar_coche_por_matricula_falla_si_no_existe():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)

    # When
    resultado = service.avanzar_coche_por_matricula("NOEXISTE", 10)

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "COCHE_NO_ENCONTRADO"


def test_obtener_info_avance_por_matricula_combustion():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)
    coche = CocheCombustion("1212AAA", "Seat")
    coche.repostar(5)
    concesionario.agregar_coche(coche)

    # When
    resultado = service.obtener_info_avance_por_matricula("1212AAA")

    # Then
    assert resultado.ok is True
    detalle = resultado.valor["detalles"][0]
    assert detalle["fuente"] == "gasolina"
    assert detalle["consumo_por_km"] == CocheCombustion.CONSUMO_LITROS_POR_KM
    assert round(detalle["km_maximos"], 2) == 100.0


def test_obtener_info_avance_por_matricula_falla_si_no_existe():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionConcesionarioService(concesionario)

    # When
    resultado = service.obtener_info_avance_por_matricula("MISSING")

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "COCHE_NO_ENCONTRADO"


