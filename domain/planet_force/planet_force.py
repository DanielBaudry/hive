from domain.unit.unit import Unit


class PlanetForce:
    def __init__(self, planet_id: int, unit: Unit, quantity: int = 0):
        self.planet_id = planet_id
        self.unit = unit
        self.quantity = quantity
