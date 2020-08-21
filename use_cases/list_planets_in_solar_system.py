from typing import List

from domain.planet.planet import Planet
from domain.planet.planet_repository import PlanetRepository


class ListPlanetsInSolarSystem:
    def __init__(self, planet_repostiory: PlanetRepository):
        self.planet_repostiory = planet_repostiory

    def execute(self, solar_system: int) -> List[Planet]:
        return self.planet_repostiory.get_planets_for_solar_system(solar_system_id=solar_system)
