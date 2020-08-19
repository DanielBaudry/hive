from abc import abstractmethod
from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.unit.unit import Unit


class HiveUnitRepository:
    @abstractmethod
    def get_all_hive_units_for_user(self, user_id: int) -> List[HiveUnit]:
        pass

    @abstractmethod
    def add_hive_units(self, user_id: int, unit_name: str, quantity: int):
        pass
