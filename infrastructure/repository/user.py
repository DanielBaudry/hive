from typing import Optional

import bcrypt

from domain.user import User
from infrastructure.repository.db import db
from infrastructure.repository.models.user import UserModel


class UserRepository(object):
    def __init__(self, database: db = db):
        self.db = database

    def save(self, user: User) -> User:
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.session.query(UserModel).get(user_id)

    def get_user_with_credentials(self, username: str, password: str) -> Optional[User]:
        user = self.db.session.query(UserModel).filter(UserModel.username == username).first()
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password) == user.password:
            return user
        return None
