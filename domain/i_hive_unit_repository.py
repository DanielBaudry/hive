from abc import abstractmethod
from typing import List

from domain.hive_unit import HiveUnit


class IHiveUnitRepository:
    @abstractmethod
    def get_all_hive_units_for_user(self, user_id: int) -> List[HiveUnit]:
        pass
