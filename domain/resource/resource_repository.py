from abc import abstractmethod, ABC
from typing import List

from domain.resource.resource import Resource


class ResourceRepository(ABC):
    @abstractmethod
    def get_resources(self, user_id: int) -> List[Resource]:
        pass
