from oop import fly_mixin
from oop.creature import Creature
from oop.fly_mixin import FlyMixin


class Phoenix(FlyMixin, Creature):

    _total_phoenixes : int = 0

    def __init__(self, name , species, origin, power_level):
        super().__init__(name=name,species= species, origin=origin, power_level=power_level)

        self.__resurrection_count = 0

        type(self)._total_phoenixes += 1

    def __str__(self):
        base = super().__str__()
        return f"{base}"

    @property
    def resurrection_count(self) -> int:
        return self.__resurrection_count

    @classmethod
    def get_total_creatures(cls) -> None:
        print("Total Phoenixes:", cls._total_phoenixes)

    def mission_duration_days(self) -> int:
        return 7

    def describe_abilities(self) -> None:
        print(f"{self.name} has a flame aura and has the ability to fly. "
                f"{self.name} can also resurrect upon death.")

    def death(self) -> None:
        print(f"{self.name} failed the mission and died bursting to flames.")
        self.resurrect()

    def resurrect(self) -> None:
        self.__resurrection_count += 1
        print(f"{self.name} resurrects from its ashes.")