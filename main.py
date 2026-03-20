"""Punto de entrada de la aplicacion.

Ejemplo:
    $ python main.py
"""

from entities.concesionario import Concesionario
from services.gestion_concesionario_service import GestionConcesionarioService
from services.gestion_personas_service import GestionPersonasService
from services.seed_data_service import SeedDataService
from ui.menu import MenuCLI


def main():
    """Construye dependencias y arranca la UI."""
    concesionario = Concesionario("Coches2026")
    concesionario_service = GestionConcesionarioService(concesionario)
    personas_service = GestionPersonasService(concesionario)

    # El seed se ejecuta aqui para tener datos demo desde el primer menu.
    seed_service = SeedDataService(concesionario_service, personas_service)
    seed_service.cargar_datos_demo()

    menu = MenuCLI(concesionario_service, personas_service)
    menu.ejecutar()


if __name__ == "__main__":
    main()

