from flask_login import UserMixin
from sqlalchemy import Column, String, Binary, Integer

from models.model import Model


class User(Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(20), nullable=False, unique=True)

    password = Column(Binary(60), nullable=False)
