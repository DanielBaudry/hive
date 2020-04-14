from domain.planet import Planet
from domain.unit import Unit


class HiveUnit:
    def __init__(self, unit: Unit, planet: Planet, quantity: int):
        self.unit = unit
        self.planet = planet
        self.quantity = quantity

