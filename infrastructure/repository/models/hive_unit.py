from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from infrastructure.repository.models.model import Model
from infrastructure.repository.models.planet import PlanetModel
from infrastructure.repository.models.unit import UnitModel


class HiveUnitModel(Model):
    __tablename__ = 'hive_unit'

    id = Column(Integer, primary_key=True, autoincrement=True)

    unitId = Column(Integer, ForeignKey("unit.id"), nullable=False, index=True)

    unit = relationship(UnitModel, foreign_keys=[unitId], backref='units')

    planetId = Column(Integer, ForeignKey("planet.id"), nullable=False, index=True)

    planet = relationship(PlanetModel, foreign_keys=[planetId], backref='hiveUnits')

    quantity = Column(Integer, nullable=True)
