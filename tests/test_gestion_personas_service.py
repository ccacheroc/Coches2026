from entities.coche_combustion import CocheCombustion
from entities.concesionario import Concesionario
from entities.persona import Persona
from services.gestion_personas_service import GestionPersonasService


def test_alta_cliente_sin_coche():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionPersonasService(concesionario)

    # When
    resultado = service.alta_cliente("1", "Ana", "Lopez")

    # Then
    assert resultado.ok is True
    cliente = concesionario.buscar_cliente_por_dni("1")
    assert cliente is not None
    assert cliente.coche is None


def test_alta_cliente_con_matricula_libre():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)
    service = GestionPersonasService(concesionario)

    # When
    resultado = service.alta_cliente("1", "Ana", "Lopez", matricula="1111AAA")

    # Then
    assert resultado.ok is True
    cliente = concesionario.buscar_cliente_por_dni("1")
    assert cliente is not None
    assert cliente.coche is coche


def test_alta_cliente_falla_si_matricula_no_existe():
    # Given
    concesionario = Concesionario("Demo")
    service = GestionPersonasService(concesionario)

    # When
    resultado = service.alta_cliente("1", "Ana", "Lopez", matricula="NOEXISTE")

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "MATRICULA_NO_ENCONTRADA"


def test_alta_cliente_falla_si_matricula_esta_ocupada():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)

    propietario = Persona("10", "Luis", "Perez", coche)
    concesionario.anadir_cliente(propietario)

    service = GestionPersonasService(concesionario)

    # When
    resultado = service.alta_cliente("20", "Ana", "Lopez", matricula="1111AAA")

    # Then
    assert resultado.ok is False
    assert resultado.codigo == "MATRICULA_OCUPADA"
    assert "10" in resultado.mensaje
    assert "transfer" in resultado.mensaje.lower()


def test_modificar_cliente_actualiza_datos_y_coche():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)
    concesionario.anadir_cliente(Persona("1", "Ana", "Lopez"))
    service = GestionPersonasService(concesionario)

    # When
    resultado = service.modificar_cliente("1", "Ana Maria", "Garcia", matricula="1111AAA")

    # Then
    assert resultado.ok is True
    cliente = concesionario.buscar_cliente_por_dni("1")
    assert cliente is not None
    assert cliente.nombre == "Ana Maria"
    assert cliente.apellido == "Garcia"
    assert cliente.coche is coche


def test_listar_clientes_con_coche_devuelve_vista_para_ui():
    # Given
    concesionario = Concesionario("Demo")
    coche = CocheCombustion("1111AAA", "Seat")
    concesionario.agregar_coche(coche)
    concesionario.anadir_cliente(Persona("1", "Ana", "Lopez", coche))
    service = GestionPersonasService(concesionario)

    # When
    clientes = service.listar_clientes_con_coche()

    # Then
    assert len(clientes) == 1
    assert clientes[0]["dni"] == "1"
    assert clientes[0]["matricula"] == "1111AAA"


