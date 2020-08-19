from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.unit.unit import Unit


def serialize_hive_units(hive_units: List[HiveUnit], units: List[Unit]):
    serialized_hive_units = []
    for unit in units:
        quantity = sum([hive_unit.quantity for hive_unit in hive_units if hive_unit.unit.name == unit.name], 0)
        serialized_hive_units.append(
            {
                'name': unit.name,
                'display_name': unit.display_name,
                'quantity': quantity,
            }
        )
    return serialized_hive_units
