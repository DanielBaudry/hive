from typing import List

from domain.hive_unit.hive_unit import HiveUnit
from domain.hive_unit.hive_unit_repository import HiveUnitRepository
from domain.unit.unit_repository import UnitRepository
from infrastructure.repository.db import db
from infrastructure.repository.hive_unit.hive_unit_domain_converter import to_domain
from infrastructure.repository.hive_unit.hive_unit_sql import HiveUnitSQL
from infrastructure.repository.user.user_sql import UserSQL


class HiveUnitSQLRepository(HiveUnitRepository):
    def __init__(self, unit_repository: UnitRepository):
        self.unit_repository = unit_repository

    def get_all_hive_units_for_user(self, user_id: int) -> List[HiveUnit]:
        hive_unit_models = db.session.query(HiveUnitSQL) \
            .join(UserSQL) \
            .filter(UserSQL.id == user_id) \
            .all()
        return [to_domain(hive_unit=hive_unit_model, unit_repository=self.unit_repository) for hive_unit_model in
                hive_unit_models]

    def add_hive_units(self, user_id: int, unit_name: str, quantity: int):
        user_hive_unit = HiveUnitSQL.query \
            .filter(HiveUnitSQL.userId == user_id) \
            .filter(HiveUnitSQL.unit_name == unit_name) \
            .first()

        if not user_hive_unit:
            user_hive_unit = HiveUnitSQL(
                user_id=user_id,
                unit_name=unit_name
            )

        user_hive_unit.quantity += quantity
        db.session.add(user_hive_unit)
        db.session.commit()
