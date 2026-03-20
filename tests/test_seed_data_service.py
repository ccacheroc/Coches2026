from entities.concesionario import Concesionario
from services.gestion_concesionario_service import GestionConcesionarioService
from services.gestion_personas_service import GestionPersonasService
from services.seed_data_service import SeedDataService


def test_seed_carga_datos_demo_en_concesionario_vacio():
    # Given
    concesionario = Concesionario("Demo")
    concesionario_service = GestionConcesionarioService(concesionario)
    personas_service = GestionPersonasService(concesionario)
    seed_service = SeedDataService(concesionario_service, personas_service)

    # When
    resultado = seed_service.cargar_datos_demo()

    # Then
    assert resultado.ok is True
    resumen = concesionario_service.resumen()
    assert resumen["num_coches"] == 5
    assert resumen["num_clientes"] == 4

    clientes = personas_service.listar_clientes_con_coche()
    con_coche = [fila for fila in clientes if fila["matricula"] is not None]
    assert len(con_coche) >= 1


def test_seed_no_duplica_datos_si_se_ejecuta_dos_veces():
    # Given
    concesionario = Concesionario("Demo")
    concesionario_service = GestionConcesionarioService(concesionario)
    personas_service = GestionPersonasService(concesionario)
    seed_service = SeedDataService(concesionario_service, personas_service)

    # When
    primero = seed_service.cargar_datos_demo()
    resumen_primero = concesionario_service.resumen()
    segundo = seed_service.cargar_datos_demo()
    resumen_segundo = concesionario_service.resumen()

    # Then
    assert primero.ok is True
    assert segundo.ok is True
    assert resumen_primero == resumen_segundo

