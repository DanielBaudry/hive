from typing import Dict

from domain.unit.unit import Unit


def to_domain(unit_detail: Dict) -> Unit:
    return Unit(
        name=unit_detail.name,
        display_name=unit_detail.value['display_name'],
        cost=unit_detail.value['cost'],
        life=unit_detail.value['life'],
        damage=unit_detail.value['damage'],
    )
