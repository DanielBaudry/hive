from abc import abstractmethod, ABC
from typing import List

from domain.planet.planet import Planet


class PlanetRepository(ABC):
    @abstractmethod
    def get_planets_for_solar_system(self, solar_system_id: int) -> List[Planet]:
        pass
