from typing import List

from models.hive_unit import HiveUnit
from models.planet import Planet
from models.user import User
from repository.db import db


class HiveUnitRepository(object):
    def __init__(self, database: db = db):
        self.db = database

    def save(self, hive_unit: HiveUnit) -> HiveUnit:
        self.db.session.add(hive_unit)
        self.db.session.commit()
        return hive_unit

    def get_all_hive_units_for_user(self, user_id: int) -> List[HiveUnit]:
        return self.db.session.query(HiveUnit) \
            .join(Planet) \
            .join(User) \
            .filter(User.id == user_id) \
            .all()
