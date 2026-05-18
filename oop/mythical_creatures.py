class Creature:
    """
    class that represents a creature
    """
    __total_creatures = 0
    __VALID_SPECIES = ["Dragon", "Ice Dragon", "Phoenix", "Griffin", "Unicorn", "Basilisk"]

    """
    ==Constructor==
    """
    def __init__(self, name: str, species: str, origin: str, power_level: int) -> None:

        self.name = name
        self.species = species
        self.origin = origin
        self.power_level = power_level
        self.__in_stable = True

        type(self).__total_creatures += 1

    #Display Name, Specie, Origin and status of the creature when using print()
    def __str__(self):
        status = "In Stable" if self.__in_stable else "On Mission"
        return f"{self._name} - {self._species} - (origin: {self._origin!r}) [{status}]"

    """
    ==Get - Set==
    """
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        if name == "":
            raise ValueError("You must provide a name")
        else:
            self._name = name

    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, species: str) -> None:
        status = type(self).is_valid_species(species)
        if not status:
            raise ValueError("Invalid species")
        else:
            self._species = species

    @property
    def origin(self) -> str:
        return self._origin
    @origin.setter
    def origin(self, origin: str) -> None:
        if origin == "":
            raise ValueError("You must provide a origin")
        else:
            self._origin = origin

    @property
    def power_level(self) -> int:
        return self._power_level
    @power_level.setter
    def power_level(self, power_level: int) -> None:
        status = type(self).is_valid_power_level(power_level)
        if not status:
            raise ValueError("Power level must be between 1 and 100")
        else:
            self._power_level = power_level

    """
    ==Methods==
    """
    def send_on_mission(self) -> None:
        self.__in_stable = False

    def return_to_stable(self) -> None:
        self.__in_stable = True

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
    def is_valid_power_level(level: int) -> bool:
        return level > 0 or level < 100


    """
    ==TEST==
    """

c1 = Creature("Glacius", species="Ice Dragon", origin="Nordic Mountains", power_level=1)
c2 = Creature("Rainbow", species="Unicorn", origin="Mist Forest", power_level=1)
c3 = Creature("Marco", species="Phoenix", origin="Wild Plains", power_level=1)
c2.send_on_mission()
Creature.get_total_creatures()
print(c1)
print(c2)
print(c3)
