"""Menu CLI del proyecto.

Ejemplo:
    >>> # main.py usa MenuCLI(...).ejecutar()
"""

class MenuCLI:
    """Interfaz de consola delgada para invocar servicios."""

    def __init__(self, concesionario_service, personas_service):
        self._concesionario_service = concesionario_service
        self._personas_service = personas_service

    def ejecutar(self):
        """Lanza bucle principal del menu CLI."""
        while True:
            print("\n=== Menu Principal Concesionario ===")
            print("1. Gestion Clientes")
            print("2. Gestion Coches")
            print("3. Transferir coche entre clientes")
            print("4. Ver Estado del Concesionario")
            print("0. Salir")

            opcion = input("Selecciona opcion: ").strip()
            if opcion == "1":
                self._menu_clientes()
            elif opcion == "2":
                self._menu_coches()
            elif opcion == "3":
                self._transferir_coche()
            elif opcion == "4":
                self._menu_estado()
            elif opcion == "0":
                print("Hasta luego.")
                return
            else:
                print("Opcion no valida.")

    def _menu_clientes(self):
        while True:
            print("\n--- Gestion Clientes ---")
            print("1. Alta cliente")
            print("2. Baja cliente")
            print("3. Modificar cliente")
            print("4. Listar clientes")
            print("0. Volver")

            opcion = input("Selecciona opcion: ").strip()
            if opcion == "1":
                self._alta_cliente()
            elif opcion == "2":
                self._baja_cliente()
            elif opcion == "3":
                self._modificar_cliente()
            elif opcion == "4":
                self._mostrar_clientes()
            elif opcion == "0":
                return
            else:
                print("Opcion no valida.")

    def _menu_coches(self):
        while True:
            print("\n--- Gestion Coches ---")
            print("1. Alta coche")
            print("2. Baja coche")
            print("3. Modificar coche")
            print("4. Listar coches")
            print("5. Avanzar coche")
            print("6. Repostar/Recargar coche")
            print("7. Ver kilometros por marca")
            print("0. Volver")

            opcion = input("Selecciona opcion: ").strip()
            if opcion == "1":
                self._alta_coche()
            elif opcion == "2":
                self._baja_coche()
            elif opcion == "3":
                self._modificar_coche()
            elif opcion == "4":
                self._mostrar_coches()
            elif opcion == "5":
                self._avanzar_coche()
            elif opcion == "6":
                self._cargar_energia_coche()
            elif opcion == "7":
                self._mostrar_kilometros_por_marca()
            elif opcion == "0":
                return
            else:
                print("Opcion no valida.")

    def _menu_estado(self):
        while True:
            print("\n--- Estado del Concesionario ---")
            print("1. Ver lista de clientes")
            print("2. Ver lista de coches")
            print("3. Ver kilometros por marca")
            print("0. Volver")

            opcion = input("Selecciona opcion: ").strip()
            if opcion == "1":
                self._mostrar_clientes()
            elif opcion == "2":
                self._mostrar_coches()
            elif opcion == "3":
                self._mostrar_kilometros_por_marca()
            elif opcion == "0":
                return
            else:
                print("Opcion no valida.")

    def _alta_cliente(self):
        dni = input("DNI: ").strip()
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        matricula = input("Matricula del coche (None/vacio si no tiene): ").strip()
        if not matricula or matricula.lower() == "none":
            matricula = None

        resultado = self._personas_service.alta_cliente(
            dni,
            nombre,
            apellido,
            matricula=matricula,
        )
        print(resultado.mensaje)

    def _baja_cliente(self):
        dni = input("DNI del cliente a dar de baja: ").strip()
        resultado = self._personas_service.baja_cliente(dni)
        print(resultado.mensaje)

    def _modificar_cliente(self):
        dni = input("DNI del cliente a modificar: ").strip()
        nombre = input("Nuevo nombre: ").strip()
        apellido = input("Nuevo apellido: ").strip()
        matricula = input("Nueva matricula (None/vacio si no tiene): ").strip()
        if not matricula or matricula.lower() == "none":
            matricula = None

        resultado = self._personas_service.modificar_cliente(
            dni,
            nombre,
            apellido,
            matricula=matricula,
        )
        print(resultado.mensaje)

    def _alta_coche(self):
        tipo = input("Tipo [combustion/electrico/hibrido]: ").strip().lower()
        matricula = input("Matricula: ").strip()
        marca = input("Marca: ").strip()

        resultado = self._concesionario_service.alta_coche(tipo, matricula, marca)
        print(resultado.mensaje)

    def _baja_coche(self):
        matricula = input("Matricula del coche a dar de baja: ").strip()
        resultado = self._concesionario_service.baja_coche_por_matricula(matricula)
        print(resultado.mensaje)

    def _modificar_coche(self):
        matricula = input("Matricula del coche a modificar: ").strip()
        nueva_marca = input("Nueva marca: ").strip()
        resultado = self._concesionario_service.modificar_coche(matricula, nueva_marca)
        print(resultado.mensaje)

    def _avanzar_coche(self):
        matricula = input("Matricula del coche a avanzar: ").strip()
        info = self._concesionario_service.obtener_info_avance_por_matricula(matricula)
        if not info.ok:
            print(info.mensaje)
            return

        valor = info.valor
        print(f"\nInfo de avance para {valor['matricula']} ({valor['tipo']}):")
        for detalle in valor["detalles"]:
            print(
                f"- Energia disponible ({detalle['fuente']}): "
                f"{detalle['energia_disponible']:.2f} {detalle['unidad_energia']}"
            )
            print(
                f"  Consumo: {detalle['consumo_por_km']:.2f} "
                f"{detalle['unidad_consumo']}"
            )
            print(f"  Maximo avance con {detalle['fuente']}: {detalle['km_maximos']:.2f} km")

        print(f"Maximo avance posible en una llamada: {valor['km_maximos']:.2f} km")
        km = input("Kilometros a avanzar: ").strip()
        resultado = self._concesionario_service.avanzar_coche_por_matricula(matricula, km)
        print(resultado.mensaje)

    def _cargar_energia_coche(self):
        matricula = input("Matricula del coche a repostar/recargar: ").strip()
        tipo_resultado = self._concesionario_service.obtener_tipo_coche_por_matricula(matricula)
        if not tipo_resultado.ok:
            print(tipo_resultado.mensaje)
            return

        tipo = tipo_resultado.valor
        if tipo == "CocheHibrido":
            litros = input("Litros de gasolina a repostar: ").strip()
            kwh = input("kWh a recargar: ").strip()
            resultado = self._concesionario_service.cargar_energia_coche_por_matricula(
                matricula,
                litros=litros,
                kwh=kwh,
            )
        elif tipo == "CocheElectrico":
            kwh = input("kWh a recargar: ").strip()
            resultado = self._concesionario_service.cargar_energia_coche_por_matricula(
                matricula,
                kwh=kwh,
            )
        else:
            litros = input("Litros de gasolina a repostar: ").strip()
            resultado = self._concesionario_service.cargar_energia_coche_por_matricula(
                matricula,
                litros=litros,
            )

        print(resultado.mensaje)

    def _transferir_coche(self):
        dni_vendedor = input("DNI vendedor: ").strip()
        dni_comprador = input("DNI comprador: ").strip()
        resultado = self._personas_service.transferir_coche(dni_vendedor, dni_comprador)
        print(resultado.mensaje)

    def _mostrar_clientes(self):
        clientes = self._personas_service.listar_clientes_con_coche()
        if not clientes:
            print("No hay clientes.")
            return

        print("\nClientes:")
        for cliente in clientes:
            matricula = cliente["matricula"] if cliente["matricula"] else "sin coche"
            print(
                f"- DNI {cliente['dni']} | {cliente['nombre']} {cliente['apellido']} "
                f"| Coche: {matricula}"
            )

    def _mostrar_coches(self):
        coches = self._concesionario_service.listar_coches_con_cliente()
        if not coches:
            print("No hay coches.")
            return

        print("\nCoches:")
        for coche in coches:
            propietario = coche["dni_propietario"] if coche["dni_propietario"] else "libre"
            print(
                f"- {coche['matricula']} | {coche['marca']} | {coche['tipo']} "
                f"| Cliente: {propietario}"
            )

    def _mostrar_kilometros_por_marca(self):
        filas = self._concesionario_service.listar_kilometros_por_marca()
        if not filas:
            print("No hay kilometros acumulados por marca.")
            return

        print("\nKilometros por marca:")
        for fila in filas:
            print(f"- {fila['marca']}: {fila['kilometros']:.2f} km")

