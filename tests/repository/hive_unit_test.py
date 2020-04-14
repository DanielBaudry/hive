import bcrypt

from infrastructure.repository.models import User
from infrastructure.repository.hive_unit_repository import HiveUnitRepository
from infrastructure.repository.user import UserRepository
from tests.conftest import clean_database


class GetAllUnitsTest:
    @clean_database
    def test_should_return_all_units_for_current_user(self, app):
        # Given
        user = create_user()
        user = UserRepository().save(user)

        # When
        hive_units = HiveUnitRepository().get_all_hive_units_for_user(user.id)

        # Then
        assert hive_units == []


def create_user(username: str = 'Test', password: str = 'password') -> User:
    user = User()
    user.username = username
    user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return user
