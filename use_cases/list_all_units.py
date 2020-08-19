from typing import List

from domain.unit.unit import Unit
from domain.unit.unit_repository import UnitRepository


class ListAllUnits:
    def __init__(self, unit_repostiory: UnitRepository):
        self.unit_repostiory = unit_repostiory

    def execute(self) -> List[Unit]:
        return self.unit_repostiory.get_all_units()
