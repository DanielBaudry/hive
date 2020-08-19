from typing import List

from domain.resource.resource import Resource
from domain.resource.resource_repository import ResourceRepository


class GetUserResources:
    def __init__(self, resource_repository: ResourceRepository):
        self.resource_repository = resource_repository

    def execute(self, user_id: int) -> List[Resource]:
        return self.resource_repository.get_resources(user_id=user_id)
