from domain.hive_unit.hive_unit_repository import HiveUnitRepository
from domain.resource.resource_repository import ResourceRepository
from domain.unit.unit_repository import UnitRepository
from domain.user_with_resources.user_with_resources import UserWithResources
from domain.user_with_resources.user_with_resources_repository import UserWithResourcesRepository
from infrastructure.repository.user_with_resources.user_with_resources_domain_converter import to_domain


class UserWithResourcesSQLRepository(UserWithResourcesRepository):
    def __init__(self, resource_repository: ResourceRepository, hive_units_repository: HiveUnitRepository,
                 unit_repository: UnitRepository):
        self.hive_units_repository = hive_units_repository
        self.unit_repository = unit_repository
        self.resource_repository = resource_repository

    def get_by_user_id(self, user_id) -> UserWithResources:
        resources = self.resource_repository.get_resources(user_id)
        hive_units = self.hive_units_repository.get_all_hive_units_for_user(user_id)
        units = self.unit_repository.get_all_units()
        return to_domain(user_id=user_id,
                         resources=resources,
                         hive_units=hive_units,
                         units=units)

    def save(self, user_with_resources: UserWithResources):
        for hive_unit in user_with_resources.hive_units:
            self.hive_units_repository.save(user_id=user_with_resources.identifier,
                                            unit_name=hive_unit.unit.name,
                                            quantity=hive_unit.quantity)
        for resource in user_with_resources.resources:
            self.resource_repository.save(resource)
