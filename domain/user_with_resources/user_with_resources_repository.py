from abc import abstractmethod, ABC

from domain.user_with_resources.user_with_resources import UserWithResources


class UserWithResourcesRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, user_id) -> UserWithResources:
        pass

    @abstractmethod
    def save(self, user_with_resources: UserWithResources):
        pass
