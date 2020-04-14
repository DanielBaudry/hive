from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from infrastructure.repository.models.model import Model
from infrastructure.repository.models.user import UserModel


class PlanetModel(Model):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(40), nullable=False)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship(UserModel, foreign_keys=[userId], backref='planets')
