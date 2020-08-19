from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.hive_unit.hive_unit_repository import HiveUnitRepository


class SpawnNewHiveUnits:
    def __init__(self, hive_unit_repostiory: HiveUnitRepository):
        self.hive_unit_repostiory = hive_unit_repostiory

    def execute(self, user_id: int, unit_name: str, quantity: int) -> List[HiveUnit]:
        return self.hive_unit_repostiory.add_hive_units(user_id=user_id, unit_name=unit_name, quantity=quantity)
