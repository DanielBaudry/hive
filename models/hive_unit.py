from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.model import Model
from models.planet import Planet
from models.unit import Unit


class HiveUnit(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)

    unitId = Column(Integer, ForeignKey("unit.id"), nullable=False, index=True)

    unit = relationship(Unit, foreign_keys=[unitId], backref='units')

    planetId = Column(Integer, ForeignKey("planet.id"), nullable=False, index=True)

    planet = relationship(Planet, foreign_keys=[planetId], backref='hiveUnits')

    quantity = Column(Integer, nullable=True)
