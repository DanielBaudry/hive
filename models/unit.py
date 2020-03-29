from sqlalchemy import Column, String, Integer

from models.model import Model


class Unit(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(140), nullable=False)
