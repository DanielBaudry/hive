from typing import List

from domain.i_hive_unit_repository import IHiveUnitRepository
from domain.hive_unit import HiveUnit
from infrastructure.repository.models.hive_unit import HiveUnitModel
from infrastructure.repository.models.planet import PlanetModel
from infrastructure.repository.models.user import UserModel
from infrastructure.repository.db import db


class HiveUnitRepository(IHiveUnitRepository):
    def __init__(self, database: db = db):
        self.db = database

    def save(self, hive_unit: HiveUnit) -> HiveUnit:
        self.db.session.add(hive_unit)
        self.db.session.commit()
        return hive_unit

    def get_all_hive_units_for_user(self, user_id: int) -> List[HiveUnit]:
        return self.db.session.query(HiveUnitModel) \
            .join(PlanetModel) \
            .join(UserModel) \
            .filter(UserModel.id == user_id) \
            .all()

    def DTOtoDomain(self, hive_unit_model: HiveUnitModel) -> HiveUnit:
        unit = HiveUnit()
        unit.name = hive_unit_model.name
        return unit
