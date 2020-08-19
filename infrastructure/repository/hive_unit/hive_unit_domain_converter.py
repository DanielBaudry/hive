from domain.hive_unit.hive_unit import HiveUnit
from domain.unit.unit_repository import UnitRepository
from infrastructure.repository.hive_unit.hive_unit_sql import HiveUnitSQL


def to_domain(hive_unit: HiveUnitSQL, unit_repository: UnitRepository) -> HiveUnit:
    unit = unit_repository.find_by_name(hive_unit.unit_name)
    return HiveUnit(
        user_id=hive_unit.userId,
        quantity=hive_unit.quantity,
        unit=unit,
    )
