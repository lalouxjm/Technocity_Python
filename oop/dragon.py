from oop.creature import Creature

class Dragon(Creature):

    _total_dragons = 0

    def __init__(self, name , species, origin, power_level, element: str):
        super().__init__(name, species, origin, power_level)

        self._element = None
        self.element = element

        type(self)._total_dragons += 1

    def __str__(self):
        base = super().__str__()
        return f"{base} - Element:[{self.element}]"

    @property
    def element(self):
        return self._element
    @element.setter
    def element(self,element):
        is_a_string = isinstance(element, str)
        if not is_a_string:
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

