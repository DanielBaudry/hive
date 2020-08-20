from typing import Dict, List

from domain.hive_unit.hive_unit import HiveUnit
from domain.resource.resource import Resource
from domain.unit.unit import Unit
from domain.user_with_resources.user_with_resources import UserWithResources


def to_domain(user_id: int, resources: List[Resource], hive_units: List[HiveUnit],
              units: List[Unit]) -> UserWithResources:
    return UserWithResources(
        identifier=user_id,
        resources=resources,
        hive_units=hive_units,
        available_units=units
    )
