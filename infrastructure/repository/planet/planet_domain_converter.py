from typing import Dict

from domain.planet.planet import Planet


def to_domain(solar_system_id: int, planet_detail: Dict) -> Planet:
    return Planet(
        identifier=planet_detail['id'],
        solar_system=solar_system_id,
        solar_system_position=planet_detail['position'],
    )
