from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.repository.model import Model
from infrastructure.repository.user.user_sql import UserSQL


class HiveUnitSQL(Model):
    __tablename__ = 'hive_unit'

    id = Column(Integer, primary_key=True, autoincrement=True)

    unit_name = Column(String(50), nullable=False)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship(UserSQL, foreign_keys=[userId])

    quantity = Column(Integer, nullable=False)

    def __init__(self, user_id: int, unit_name: str, quantity: int = 0):
        self.userId = user_id
        self.unit_name = unit_name
        self.quantity = quantity
