from typing import List

from domain.resource.resource import Resource
from domain.resource.resource_repository import ResourceRepository
from infrastructure.repository.resource.resource_domain_converter import to_domain
from infrastructure.repository.resource.resource_sql import ResourceSQL


class ResourceSQLRepository(ResourceRepository):
    def get_resources(self, user_id: int) -> List[Resource]:
        resources_sql = ResourceSQL.query.filter(
            ResourceSQL.userId == user_id
        ).all()
        return [to_domain(resource_sql) for resource_sql in resources_sql]
