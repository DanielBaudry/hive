from typing import List

from domain.hive_unit import HiveUnit
from domain.i_hive_unit_repository import IHiveUnitRepository


class GetAllHiveUnits:
    def __init__(self, i_hive_unit_repository: IHiveUnitRepository):
        self.i_hive_unit_repository = i_hive_unit_repository

    def get_all_hive_units(self, user_id: int) -> List[HiveUnit]:
        return self.i_hive_unit_repository.get_all_hive_units_for_user(user_id)
