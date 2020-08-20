from domain.resource.resource import Resource
from infrastructure.repository.resource.resource_sql import ResourceSQL


def to_domain(resource_sql: ResourceSQL) -> Resource:
    return Resource(
        name=resource_sql.name,
        user_id=resource_sql.userId,
        amount=resource_sql.amount,
        last_update=resource_sql.last_update,
        growth_rate=resource_sql.growth_rate,
    )
