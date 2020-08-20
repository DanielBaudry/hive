from datetime import datetime


class Resource:
    def __init__(self, user_id: int, name: str, amount: int, growth_rate: float,
                 last_update: int = int(datetime.now().timestamp())):
        self.user_id = user_id
        self.name = name
        self.amount = amount
        self.growth_rate = growth_rate
        self.last_update = last_update

    @property
    def real_time_amount(self) -> int:
        return self.amount + self.delta_growth

    @property
    def delta_growth(self) -> int:
        return round((int(datetime.now().timestamp()) - self.last_update) * self.growth_rate)

    def is_enough(self, resource_cost: int) -> bool:
        return self.real_time_amount >= resource_cost

    def decrement_resource(self, resource_cost: int):
        self.amount = self.amount + self.delta_growth - resource_cost
        self.new_last_update()

    def new_last_update(self):
        self.last_update = int(datetime.now().timestamp())
