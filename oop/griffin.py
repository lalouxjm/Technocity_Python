from oop.creature import Creature

class Griffin(Creature):
    def __init__(self, name, species, origin, power_level):
        super().__init__(name, species, origin, power_level)

    def __str__(self):
        base = super().__str__()
        return f"{base}"

    def mission_duration_days(self) -> int:
        return 4

    def describe_abilities(self) -> str:
        return f"{self.name} can run fast and fly slowly."