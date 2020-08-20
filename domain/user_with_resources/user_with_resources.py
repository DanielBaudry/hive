from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.resource.resource import Resource
from domain.resource.resource_type import ResourceType
from domain.unit.unit import Unit


class UserWithResources:
    def __init__(self, identifier: int,
                 resources: List[Resource],
                 hive_units: List[HiveUnit],
                 available_units: List[Unit]):
        self.identifier = identifier
        self.resources = resources
        self.available_units = available_units
        self.hive_units = hive_units

    def spawn_hive_unit(self, unit_name: str, quantity: int):
        unit_to_spawn = next(iter([unit for unit in self.available_units if unit.name == unit_name]))
        resource_cost = quantity * unit_to_spawn.cost
        needed_unit_resource = next(
            iter([resource for resource in self.resources if resource.name == ResourceType.LARVAE]))

        if needed_unit_resource.is_enough(resource_cost):
            self.increment_hive_unit_number(unit_to_spawn, quantity)
            needed_unit_resource.decrement_resource(resource_cost)

    def increment_hive_unit_number(self, unit, quantity):
        hive_unit = next(iter([hive_unit for hive_unit in self.hive_units if hive_unit.unit.name == unit.name]), None)
        if not hive_unit:
            hive_unit = HiveUnit(
                user_id=self.identifier,
                unit=unit,
            )
        hive_unit.increment_number(quantity)
        self.hive_units.append(hive_unit)
