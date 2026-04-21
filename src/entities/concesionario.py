"""Entidad agregadora para inventario y clientes.

Ejemplo:
    >>> concesionario = Concesionario("Autos Demo")
"""


from src.entities.resultado import Resultado


class Concesionario:
    """Gestiona coches y clientes del concesionario."""

    def __init__(self, nombre, coches=None, clientes=None):
        self.__nombre = str(nombre)
        self.__coches = list(coches) if coches else []
        self.__clientes = list(clientes) if clientes else []
        self.__ultimo_resultado = Resultado.exito("Sin operaciones")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def coches(self):
        return tuple(self.__coches)

    @property
    def clientes(self):
        return tuple(self.__clientes)

    @property
    def ultimo_resultado(self):
        return self.__ultimo_resultado

    def _registrar_resultado(self, resultado):
        self.__ultimo_resultado = resultado
        return resultado

    def buscar_cliente_por_dni(self, dni):
        for cliente in self.__clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def buscar_coche_por_matricula(self, matricula):
        index = self._indice_coche(matricula)
        if index is None:
            return None
        return self.__coches[index]

    def buscar_propietario_por_matricula(self, matricula):
        for cliente in self.__clientes:
            if cliente.coche is not None and cliente.coche.matricula == matricula:
                return cliente
        return None

    def anadir_cliente(self, persona):
        if self.buscar_cliente_por_dni(persona.dni) is not None:
            return self._registrar_resultado(
                Resultado.error("Ya existe un cliente con ese DNI", "DNI_DUPLICADO")
            )
        self.__clientes.append(persona)
        return self._registrar_resultado(Resultado.exito("Cliente añadido"))

    def sustituir_cliente(self, persona):
        for index, cliente in enumerate(self.__clientes):
            if cliente.dni == persona.dni:
                self.__clientes[index] = persona
                return self._registrar_resultado(Resultado.exito("Cliente sustituido"))
        return self._registrar_resultado(
            Resultado.error("Cliente inexistente", "CLIENTE_NO_ENCONTRADO")
        )

    def eliminar_cliente(self, dni):
        for index, cliente in enumerate(self.__clientes):
            if cliente.dni == dni:
                self.__clientes.pop(index)
                return self._registrar_resultado(Resultado.exito("Cliente eliminado"))
        return self._registrar_resultado(
            Resultado.error("Cliente inexistente", "CLIENTE_NO_ENCONTRADO")
        )

    def _indice_coche(self, matricula):
        for index, coche in enumerate(self.__coches):
            if coche.matricula == matricula:
                return index
        return None

    def agregar_coche(self, coche):
        if self._indice_coche(coche.matricula) is not None:
            return self._registrar_resultado(
                Resultado.error("El coche ya existe", "COCHE_DUPLICADO")
            )

        self.__coches.append(coche)
        return self._registrar_resultado(Resultado.exito("Coche añadido"))

    def eliminar_coche(self, coche):
        index = self._indice_coche(coche.matricula)
        if index is None:
            return self._registrar_resultado(
                Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")
            )

        self.__coches.pop(index)
        return self._registrar_resultado(Resultado.exito("Coche eliminado"))

    def sustituir_coche(self, coche):
        index = self._indice_coche(coche.matricula)
        if index is None:
            return self._registrar_resultado(
                Resultado.error("El coche no existe", "COCHE_NO_ENCONTRADO")
            )

        self.__coches[index] = coche
        return self._registrar_resultado(Resultado.exito("Coche sustituido"))

    def _copiar(self):
        return Concesionario(self.__nombre, coches=self.__coches, clientes=self.__clientes)

    def __getitem__(self, index):
        return self.__coches[index]

    def __len__(self):
        return len(self.__coches)

    def __bool__(self):
        return bool(self.__coches)

    def __iadd__(self, coche):
        self.agregar_coche(coche)
        return self

    def __isub__(self, coche):
        self.eliminar_coche(coche)
        return self

    def __add__(self, coche):
        nuevo = self._copiar()
        nuevo.agregar_coche(coche)
        return nuevo

    def __sub__(self, coche):
        nuevo = self._copiar()
        nuevo.eliminar_coche(coche)
        return nuevo

    def __str__(self):
        return (
            f"Concesionario({self.nombre}) - "
            f"{len(self.__coches)} coches, {len(self.__clientes)} clientes"
        )

    def __repr__(self):
        return (
            f"Concesionario({self.nombre!r}, coches={self.__coches!r}, "
            f"clientes={self.__clientes!r})"
        )

