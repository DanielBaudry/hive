class Resource:
    def __init__(self, user_id: int, name: str, amount: int):
        self.user_id = user_id
        self.name = name
        self.amount = amount

    def is_enough(self, resource_cost: int) -> bool:
        return self.amount >= resource_cost

    def decrement_resource(self, resource_cost: int):
        self.amount -= resource_cost
