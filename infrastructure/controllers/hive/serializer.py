from typing import List, Dict

from domain.hive_unit.hive_unit import HiveUnit
from domain.resource.resource import Resource
from domain.unit.unit import Unit


def serialize_resources(resources: List[Resource]) -> List[Dict]:
    serialized_resources = []
    for resource in resources:
        serialized_resources.append(
            {
                'name': resource.name.value,
                'amount': resource.amount,
            }
        )
    return serialized_resources


def serialize_hive_units(hive_units: List[HiveUnit], units: List[Unit]) -> List[Dict]:
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
