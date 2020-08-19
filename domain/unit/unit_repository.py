from abc import abstractmethod
from typing import List, Optional

from domain.unit.unit import Unit


class UnitRepository:
    @abstractmethod
    def get_all_units(self) -> List[Unit]:
        pass

    @abstractmethod
    def find_by_name(self, unit_name: str) -> Optional[Unit]:
        pass
