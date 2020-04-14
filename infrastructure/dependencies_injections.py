from infrastructure.repository.hive_unit_repository import HiveUnitRepository
from use_cases.get_all_hive_units import GetAllHiveUnits


def provide_get_all_hive_units_use_case():
    return GetAllHiveUnits(HiveUnitRepository())
