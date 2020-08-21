from typing import List

from domain.planet.planet import Planet
from domain.planet.planet_repository import PlanetRepository
from infrastructure.repository.planet.planet_domain_converter import to_domain
from infrastructure.repository.planet.solar_system_details import SolarSystemsInMemory


class PlanetInMemoryRepository(PlanetRepository):
    def __init__(self, solar_systems: List = SolarSystemsInMemory):
        self.solar_systems = solar_systems

    def get_planets_for_solar_system(self, solar_system_id: int) -> List[Planet]:
        solar_system_planets = next(iter([solar_system.value['planets'] for solar_system in self.solar_systems if
                                          solar_system.value['id'] == solar_system_id]), None)
        return [to_domain(solar_system_id, planet_detail) for planet_detail in
                solar_system_planets] if solar_system_planets else []
