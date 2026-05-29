from oop.creature import Creature
import my_func as mf
from oop.fly_mixin import FlyMixin


class Dragon(FlyMixin, Creature):

    _total_dragons = 0

    def __init__(self, name , origin, power_level, element: str):
        super().__init__(name=name,species="Dragon", origin=origin, power_level=power_level)

        self._element = None
        self.element = element

        type(self)._total_dragons += 1

    def __str__(self):
        status = mf.green("In Stable") if self._in_stable else mf.red("On Mission")
        return f"{mf.blue(self._name)} - LvL {self._power_level} {mf.yellow("<[",self.element,"]", self._species, ">")} (origin: {self._origin!r}) [{status}]"

    @property
    def element(self):
        return self._element
    @element.setter
    def element(self,element):
        if not isinstance(element, str):
            raise TypeError("Element must be a string")
        else:
            self._element = element

    def mission_duration_days(self) -> int:
        return 14

    def describe_abilities(self) -> str:
        return f"{self.name} breathes {self.element.lower()} and flies at great speed."

    @classmethod
    def get_total_creatures(cls) -> None:
        print("Total Dragons:", cls._total_dragons)

