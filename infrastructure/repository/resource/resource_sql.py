from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from domain.resource.resource_type import ResourceType
from infrastructure.repository.model import Model
from infrastructure.repository.user.user_sql import UserSQL


class ResourceSQL(Model):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(Enum(ResourceType), nullable=False)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship(UserSQL, foreign_keys=[userId])

    amount = Column(Integer, nullable=False)

    def __init__(self, user_id: int, name: str, amount: int = 0):
        self.userId = user_id
        self.name = name
        self.amount = amount
