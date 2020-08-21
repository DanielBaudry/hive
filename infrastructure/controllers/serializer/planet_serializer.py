from typing import Dict, List

from domain.planet.planet import Planet


def _serialize_planet(planet: Planet) -> Dict:
    return {
        'id': planet.identifier,
        'position': planet.solar_system_position,
    }


def serialize_planets(planets: List[Planet]):
    return [_serialize_planet(planet) for planet in planets]
