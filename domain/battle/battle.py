from typing import Optional


class Battle:
    def __init__(self, user1_id: int, planet_id: int, user2_id: Optional[int] = None):
        self.user1_id = user1_id
        self.planet_id = planet_id
        self.user2_id = user2_id

    def fight(self):
        pass
