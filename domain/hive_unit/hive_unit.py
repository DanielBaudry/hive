from domain.unit.unit import Unit


class HiveUnit:
    def __init__(self, user_id: int, unit: Unit, quantity: int):
        self.user_id = user_id
        self.unit = unit
        self.quantity = quantity
