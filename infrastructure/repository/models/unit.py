from sqlalchemy import Column, String, Integer

from infrastructure.repository.models.model import Model


class UnitModel(Model):
    __tablename__ = 'unit'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(140), nullable=False)
