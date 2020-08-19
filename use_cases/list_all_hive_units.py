from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.hive_unit.hive_unit_repository import HiveUnitRepository


class ListAllHiveUnits:
    def __init__(self, hive_unit_repostiory: HiveUnitRepository):
        self.hive_unit_repostiory = hive_unit_repostiory

    def execute(self, user_id: int) -> List[HiveUnit]:
        return self.hive_unit_repostiory.get_all_hive_units_for_user(user_id=user_id)
