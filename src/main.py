"""Punto de entrada de la aplicacion.

Ejemplo:
    $ python main.py
"""

from src.entities import Concesionario
from src.services.gestion_concesionario_service import GestionConcesionarioService
from src.services.gestion_personas_service import GestionPersonasService
from src.services.seed_data_service import SeedDataService
from src.ui.menu import MenuCLI


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

