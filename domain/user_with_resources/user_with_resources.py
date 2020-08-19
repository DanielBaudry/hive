from typing import List

from domain.resource.resource import Resource


class UserWithResources:
    def __init__(self, identifier: int, resources: List[Resource]):
        self.identifier = identifier
        self.resources = resources
