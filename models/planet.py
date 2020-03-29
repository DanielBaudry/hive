from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.model import Model


class Planet(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(40), nullable=False)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship('User', foreign_keys=[userId], backref='planets')
