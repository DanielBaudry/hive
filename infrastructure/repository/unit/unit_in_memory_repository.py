from typing import List, Optional

from domain.unit.unit import Unit
from domain.unit.unit_repository import UnitRepository
from infrastructure.repository.unit.unit_domain_converter import to_domain
from infrastructure.repository.unit.units_details import UnitsInMemory


class UnitInMemoryRepository(UnitRepository):
    def __init__(self, units: List = UnitsInMemory):
        self.units = units

    def get_all_units(self) -> List[Unit]:
        return [to_domain(unit) for unit in self.units]

    def find_by_name(self, unit_name: str) -> Optional[Unit]:
        return to_domain(next(iter([unit for unit in self.units if unit.name == unit_name]), None))
