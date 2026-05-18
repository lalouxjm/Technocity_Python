class Creature:
    """
    class that represents a creature
    """
    _total_creatures = 0

    @classmethod
    def display_all_creatures(cls) -> None:
        print("Total Creatures:", cls._total_creatures)

    def __init__(self, name: str, species: str, origin: str, power_level: int) -> None:
        self._name = name
        self._species = species
        self._origin = origin
        self._power_level = power_level
        self.__in_stable = True

        type(self)._total_creatures += 1

    #Display Name, Specie, Origin and status of the creature when using print()
    def __str__(self):
        if self.__in_stable:
            status = "In Stable"
        else:
            status = "On Mission"
        return f"{self._name} - {self._species} - (origin: {self._origin!r}) [{status}]"

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        if name is "":
            raise ValueError("You must provide a name")
        else:
            self._name = name

    @property
    def species(self) -> str:
        return self._species
    @species.setter
    def species(self, species: str) -> None:
        if species is "":
            raise ValueError("You must provide a species")
        else:
            self._species = species

    @property
    def origin(self) -> str:
        return self._origin
    @origin.setter
    def origin(self, origin: str) -> None:
        if origin is "":
            raise ValueError("You must provide a origin")
        else:
            self._origin = origin

    @property
    def power_level(self) -> int:
        return self._power_level
    @power_level.setter
    def power_level(self, power_level: int) -> None:
        if power_level <= 0 or power_level > 100:
            raise ValueError("Power level must be between 1 and 100")
        else:
            self._power_level = power_level



    def send_on_mission(self) -> None:
        self.__in_stable = False

    def return_to_stable(self) -> None:
        self.__in_stable = True



"""
==TEST==
"""
c1 = Creature("Glacius", species="Dragon", origin="Nordic Mountains", power_level=1)
c2 = Creature("Rainbow", species="Unicorn", origin="Mist Forest", power_level=1)
c3 = Creature("Melford", species="Centaur", origin="Wild Plains", power_level=1)
c2.send_on_mission()
Creature.display_all_creatures()
print(c1)
print(c2)
print(c3)
c4 = Creature("blabla","dog","house",0)
c4.display_all_creatures()

print(c4)