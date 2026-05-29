from oop.creature import Creature

class Basilisk(Creature):
    def __init__(self, name, origin, power_level):
        super().__init__(name=name, species="Basilisk", origin=origin, power_level=power_level)

    def __str__(self):
        base = super().__str__()
        return f"{base}"

    def mission_duration_days(self) -> int:
        return 10

    def describe_abilities(self) -> str:
        return f"{self.name} walks slowly and poisons its enemies."