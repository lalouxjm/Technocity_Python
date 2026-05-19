import random
from abc import ABC, abstractmethod

import my_func


class Creature(ABC):
    """
    class that represents a creature
    """
    _total_creatures = 0
    __VALID_SPECIES = ["Dragon", "Ice Dragon", "Phoenix", "Griffin", "Unicorn", "Basilisk"]

    """
    ==Constructor==
    """
    def __init__(self, name: str, species: str, origin: str, power_level: int | float) -> None:

        if origin == "":
            raise ValueError("You must provide a origin")

        #None
        self._name = None
        self._species = None
        self._power_level = None

        #Setters
        self.name = name
        self.species = species
        self.power_level = power_level

        #Privates
        self.__origin = origin
        self._in_stable = True

        Creature._total_creatures += 1

    #Display Name, Specie, Origin and status of the creature when using print()
    def __str__(self):
        status = "In Stable" if self._in_stable else "On Mission"
        return f"{my_func.blue(self._name)} - LvL {self._power_level} - {self._species} - (origin: {self.__origin!r}) [{my_func.green(status)}]" if self._in_stable \
            else f"{my_func.blue(self._name)} - LvL {self._power_level} - {self._species} - (origin: {self.__origin!r}) [{my_func.red(status)}]"

    def __repr__(self):
        return f"Creature(name={self._name!r},species={self._species!r},origin={self.__origin!r},power_level={self._power_level})"

    """
    ==Get - Set==
    """
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        is_a_str = isinstance(name, str)
        if not is_a_str:
            raise ValueError("Invalid name.\rName must be a string")
        else:
            if name == "":
                raise ValueError("You must provide a name")
            else:
                self._name = name

    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, species: str) -> None:
        is_a_str = isinstance(species, str)
        if not is_a_str:
            raise ValueError("Invalid species.\rSpecies must be a string")
        else:
            status = type(self).is_valid_species(species)
            if not status:
                raise ValueError("Invalid species")
            else:
                self._species = species

    @property
    def origin(self) -> str:
        return self.__origin
    """
    @origin.setter
    def origin(self, origin: str) -> None:
        if origin == "":
            raise ValueError("You must provide a origin")
        else:
            self.__origin = origin
    """

    @property
    def power_level(self) -> int | float:
        return self._power_level
    @power_level.setter
    def power_level(self, power_level: int | float) -> None:
        is_a_int = isinstance(power_level, (int, float))
        if not is_a_int:
            raise ValueError("Invalid power level.\rPower level must be an int or a float.")
        else:
            status = type(self).is_valid_power_level(power_level)
            if not status:
                raise ValueError("Power level must be between 0 and 100")
            else:
                self._power_level = power_level

    """
    ==Methods==
    """
    def send_on_mission(self) -> None:
        self._in_stable = False

    def return_to_stable(self) -> None:
        self._in_stable = True

    def send_to_field(self) -> None:
        print(self.describe_abilities())
        self.send_on_mission()
        print(f"{self.name} will be gone on mission for {self.mission_duration_days()} days.")
        print(self)

    def return_from_mission(self) -> None:
        self.return_to_stable()
        print(f"{self.name} came back from his mission after {self.mission_duration_days()} days and earned {random.randint(25,75)} Exp.")

    """
    ==Class Methods==
    """
    @classmethod
    def get_total_creatures(cls) -> None:
        print("Total Creatures:", cls._total_creatures)

    @classmethod
    def add_from_dict(cls, data: dict):
        return cls(
            data["name"],
            data["species"],
            data["origin"],
            data["power_level"]
        )

    @classmethod
    def add_from_string(cls, creature_string: str):

        name, species, origin, power_level = creature_string.split(",")
        return cls(
            name,
            species,
            origin,
            int(power_level)
        )

    """
     ==Static Methods==
    """

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Creature.__VALID_SPECIES

    @staticmethod
    def is_valid_power_level(level: int | float) -> bool:
        return level > 0 or level < 100

    """
    ==Abstract Methods==
    """

    @abstractmethod
    def mission_duration_days(self) -> int:
        ...

    @abstractmethod
    def describe_abilities(self) -> str:
        ...
