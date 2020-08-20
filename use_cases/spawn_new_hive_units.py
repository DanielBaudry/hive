from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.user_with_resources.user_with_resources_repository import UserWithResourcesRepository


class SpawnNewHiveUnits:
    def __init__(self, user_with_resources_repository: UserWithResourcesRepository):
        self.user_with_resources_repository = user_with_resources_repository

    def execute(self, user_id: int, unit_name: str, quantity: int) -> List[HiveUnit]:
        user_with_resources = self.user_with_resources_repository.get_by_user_id(user_id=user_id)
        user_with_resources.spawn_hive_unit(unit_name=unit_name, quantity=quantity)
        self.user_with_resources_repository.save(user_with_resources)
        return user_with_resources.hive_units
