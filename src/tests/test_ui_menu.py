from src.entities.resultado import Resultado
from src.ui.menu import MenuCLI


class FakeConcesionarioService:
    def __init__(self):
        self.alta_args = None
        self.baja_args = None
        self.modificar_args = None
        self.avanzar_args = None
        self.info_avance_args = None
        self.cargar_energia_args = None
        self.tipo_por_matricula = "CocheCombustion"
        self.coches = []
        self.kilometros_por_marca = []

    def alta_coche(self, tipo, matricula, marca):
        self.alta_args = (tipo, matricula, marca)
        return Resultado.exito("Coche añadido")

    def baja_coche_por_matricula(self, matricula):
        self.baja_args = matricula
        return Resultado.exito("Coche eliminado")

    def modificar_coche(self, matricula, nueva_marca):
        self.modificar_args = (matricula, nueva_marca)
        return Resultado.exito("Coche modificado")

    def avanzar_coche_por_matricula(self, matricula, km):
        self.avanzar_args = (matricula, km)
        return Resultado.exito("Coche avanzado")

    def obtener_info_avance_por_matricula(self, matricula):
        self.info_avance_args = matricula
        return Resultado.exito(
            "Info OK",
            valor={
                "matricula": matricula,
                "tipo": "CocheCombustion",
                "detalles": [
                    {
                        "fuente": "gasolina",
                        "energia_disponible": 8.0,
                        "unidad_energia": "L",
                        "consumo_por_km": 0.05,
                        "unidad_consumo": "L/km",
                        "km_maximos": 160.0,
                    }
                ],
                "km_maximos": 160.0,
            },
        )

    def cargar_energia_coche_por_matricula(self, matricula, litros=None, kwh=None):
        self.cargar_energia_args = (matricula, litros, kwh)
        return Resultado.exito("Energia cargada")

    def obtener_tipo_coche_por_matricula(self, matricula):
        return Resultado.exito("Tipo OK", valor=self.tipo_por_matricula)

    def listar_coches_con_cliente(self):
        return self.coches

    def listar_kilometros_por_marca(self):
        return self.kilometros_por_marca


class FakePersonasService:
    def __init__(self):
        self.alta_args = None
        self.baja_args = None
        self.modificar_args = None
        self.transferencia_args = None
        self.clientes = []

    def alta_cliente(self, dni, nombre, apellido, matricula=None):
        self.alta_args = (dni, nombre, apellido, matricula)
        return Resultado.exito("Cliente añadido")

    def baja_cliente(self, dni):
        self.baja_args = dni
        return Resultado.exito("Cliente eliminado")

    def modificar_cliente(self, dni, nombre, apellido, matricula=None):
        self.modificar_args = (dni, nombre, apellido, matricula)
        return Resultado.exito("Cliente modificado")

    def transferir_coche(self, dni_vendedor, dni_comprador):
        self.transferencia_args = (dni_vendedor, dni_comprador)
        return Resultado.exito("Transferencia OK")

    def listar_clientes_con_coche(self):
        return self.clientes


def _input_secuencial(respuestas):
    iterator = iter(respuestas)

    def _fake_input(_prompt=""):
        return next(iterator)

    return _fake_input


def test_ejecutar_sale_con_opcion_0(monkeypatch, capsys):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    monkeypatch.setattr("builtins.input", _input_secuencial(["0"]))

    # When
    menu.ejecutar()

    # Then
    salida = capsys.readouterr().out
    assert "Menu Principal Concesionario" in salida
    assert "Hasta luego." in salida


def test_ejecutar_muestra_error_en_opcion_no_valida(monkeypatch, capsys):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    monkeypatch.setattr("builtins.input", _input_secuencial(["x", "0"]))

    # When
    menu.ejecutar()

    # Then
    salida = capsys.readouterr().out
    assert "Opcion no valida." in salida


def test_menu_principal_rutea_a_submenus_y_transferencia(monkeypatch):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    llamadas = []
    monkeypatch.setattr(menu, "_menu_clientes", lambda: llamadas.append("clientes"))
    monkeypatch.setattr(menu, "_menu_coches", lambda: llamadas.append("coches"))
    monkeypatch.setattr(menu, "_transferir_coche", lambda: llamadas.append("transferir"))
    monkeypatch.setattr(menu, "_menu_estado", lambda: llamadas.append("estado"))
    monkeypatch.setattr("builtins.input", _input_secuencial(["1", "2", "3", "4", "0"]))

    # When
    menu.ejecutar()

    # Then
    assert llamadas == ["clientes", "coches", "transferir", "estado"]


def test_submenu_clientes_opcion_listar_rutea_a_mostrar_clientes(monkeypatch):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    llamadas = []
    monkeypatch.setattr(menu, "_mostrar_clientes", lambda: llamadas.append("listar_clientes"))
    monkeypatch.setattr("builtins.input", _input_secuencial(["4", "0"]))

    # When
    menu._menu_clientes()

    # Then
    assert llamadas == ["listar_clientes"]


def test_submenu_coches_opcion_listar_rutea_a_mostrar_coches(monkeypatch):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    llamadas = []
    monkeypatch.setattr(menu, "_mostrar_coches", lambda: llamadas.append("listar_coches"))
    monkeypatch.setattr("builtins.input", _input_secuencial(["4", "0"]))

    # When
    menu._menu_coches()

    # Then
    assert llamadas == ["listar_coches"]


def test_submenu_coches_nuevas_opciones_rutean_metodos(monkeypatch):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    llamadas = []
    monkeypatch.setattr(menu, "_avanzar_coche", lambda: llamadas.append("avanzar"))
    monkeypatch.setattr(menu, "_cargar_energia_coche", lambda: llamadas.append("cargar"))
    monkeypatch.setattr(
        menu,
        "_mostrar_kilometros_por_marca",
        lambda: llamadas.append("km_marca"),
    )
    monkeypatch.setattr("builtins.input", _input_secuencial(["5", "6", "7", "0"]))

    # When
    menu._menu_coches()

    # Then
    assert llamadas == ["avanzar", "cargar", "km_marca"]


def test_submenu_estado_opcion_kilometros_rutea_a_vista(monkeypatch):
    # Given
    menu = MenuCLI(FakeConcesionarioService(), FakePersonasService())
    llamadas = []
    monkeypatch.setattr(
        menu,
        "_mostrar_kilometros_por_marca",
        lambda: llamadas.append("kilometros"),
    )
    monkeypatch.setattr("builtins.input", _input_secuencial(["3", "0"]))

    # When
    menu._menu_estado()

    # Then
    assert llamadas == ["kilometros"]


def test_alta_cliente_traduce_matricula_vacia_a_none(monkeypatch):
    # Given
    personas_service = FakePersonasService()
    menu = MenuCLI(FakeConcesionarioService(), personas_service)
    monkeypatch.setattr("builtins.input", _input_secuencial(["123", "Ana", "Lopez", ""]))

    # When
    menu._alta_cliente()

    # Then
    assert personas_service.alta_args == ("123", "Ana", "Lopez", None)


def test_modificar_cliente_envia_datos_al_servicio(monkeypatch):
    # Given
    personas_service = FakePersonasService()
    menu = MenuCLI(FakeConcesionarioService(), personas_service)
    monkeypatch.setattr(
        "builtins.input",
        _input_secuencial(["123", "Nuevo", "Apellido", "1111AAA"]),
    )

    # When
    menu._modificar_cliente()

    # Then
    assert personas_service.modificar_args == ("123", "Nuevo", "Apellido", "1111AAA")


def test_avanzar_coche_envia_datos_al_servicio(monkeypatch):
    # Given
    concesionario_service = FakeConcesionarioService()
    menu = MenuCLI(concesionario_service, FakePersonasService())
    monkeypatch.setattr("builtins.input", _input_secuencial(["1111AAA", "40"]))

    # When
    menu._avanzar_coche()

    # Then
    assert concesionario_service.info_avance_args == "1111AAA"
    assert concesionario_service.avanzar_args == ("1111AAA", "40")


def test_avanzar_coche_muestra_info_antes_de_pedir_km(monkeypatch, capsys):
    # Given
    concesionario_service = FakeConcesionarioService()
    menu = MenuCLI(concesionario_service, FakePersonasService())
    monkeypatch.setattr("builtins.input", _input_secuencial(["1111AAA", "40"]))

    # When
    menu._avanzar_coche()

    # Then
    salida = capsys.readouterr().out
    assert "Info de avance para 1111AAA" in salida
    assert "Energia disponible" in salida
    assert "Consumo:" in salida
    assert "Maximo avance posible en una llamada" in salida


def test_cargar_energia_coche_envia_datos_al_servicio(monkeypatch):
    # Given
    concesionario_service = FakeConcesionarioService()
    concesionario_service.tipo_por_matricula = "CocheElectrico"
    menu = MenuCLI(concesionario_service, FakePersonasService())
    monkeypatch.setattr(
        "builtins.input",
        _input_secuencial(["2222BBB", "12.5"]),
    )

    # When
    menu._cargar_energia_coche()

    # Then
    assert concesionario_service.cargar_energia_args == ("2222BBB", None, "12.5")


def test_cargar_energia_coche_hibrido_pide_litros_y_kwh(monkeypatch):
    # Given
    concesionario_service = FakeConcesionarioService()
    concesionario_service.tipo_por_matricula = "CocheHibrido"
    menu = MenuCLI(concesionario_service, FakePersonasService())
    monkeypatch.setattr(
        "builtins.input",
        _input_secuencial(["3333CCC", "20", "8"]),
    )

    # When
    menu._cargar_energia_coche()

    # Then
    assert concesionario_service.cargar_energia_args == ("3333CCC", "20", "8")


def test_mostrar_clientes_y_coches_en_estado(capsys):
    # Given
    concesionario_service = FakeConcesionarioService()
    personas_service = FakePersonasService()
    menu = MenuCLI(concesionario_service, personas_service)

    personas_service.clientes = [
        {"dni": "1", "nombre": "Ana", "apellido": "Lopez", "matricula": None},
        {"dni": "2", "nombre": "Luis", "apellido": "Perez", "matricula": "2222BBB"},
    ]
    concesionario_service.coches = [
        {
            "matricula": "1111AAA",
            "marca": "Seat",
            "tipo": "CocheCombustion",
            "dni_propietario": None,
        },
        {
            "matricula": "2222BBB",
            "marca": "Ford",
            "tipo": "CocheCombustion",
            "dni_propietario": "2",
        },
    ]

    # When
    menu._mostrar_clientes()
    menu._mostrar_coches()

    # Then
    salida = capsys.readouterr().out
    assert "DNI 1" in salida
    assert "sin coche" in salida
    assert "2222BBB" in salida
    assert "Cliente: libre" in salida
    assert "Cliente: 2" in salida


def test_mostrar_kilometros_por_marca_en_estado(capsys):
    # Given
    concesionario_service = FakeConcesionarioService()
    personas_service = FakePersonasService()
    menu = MenuCLI(concesionario_service, personas_service)
    concesionario_service.kilometros_por_marca = [
        {"marca": "Seat", "kilometros": 123.5},
        {"marca": "Toyota", "kilometros": 20.0},
    ]

    # When
    menu._mostrar_kilometros_por_marca()

    # Then
    salida = capsys.readouterr().out
    assert "Kilometros por marca" in salida
    assert "Seat: 123.50 km" in salida
    assert "Toyota: 20.00 km" in salida


