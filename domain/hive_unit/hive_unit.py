from domain.unit.unit import Unit


class HiveUnit:
    def __init__(self, user_id: int, unit: Unit, quantity: int = 0):
        self.user_id = user_id
        self.unit = unit
        self.quantity = quantity

    def increment_number(self, quantity: int):
        self.quantity += quantity
