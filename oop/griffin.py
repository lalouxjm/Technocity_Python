from oop.creature import Creature
from oop.fly_mixin import FlyMixin


class Griffin(FlyMixin, Creature):
    def __init__(self, name, origin, power_level):
        super().__init__(name=name,species="Griffin", origin=origin, power_level=power_level)

    def __str__(self):
        base = super().__str__()
        return f"{base}"

    def mission_duration_days(self) -> int:
        return 4

    def describe_abilities(self) -> str:
        return f"{self.name} can run fast and fly slowly."