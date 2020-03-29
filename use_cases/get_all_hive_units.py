from typing import List

from models.hive_unit import HiveUnit
from repository.hive_unit_repository import HiveUnitRepository


def get_all_hive_units(user_id: int) -> List[HiveUnit]:
    return HiveUnitRepository().get_all_hive_units_for_user(user_id)
