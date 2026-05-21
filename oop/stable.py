from typing import Iterator
from oop.creature import Creature
from oop.robotic_guard import RoboticGuard
import my_func as mf


class Stable:
    def __init__(self):
        self._creatures: list[Creature] = []
        self._robots: list[RoboticGuard] = []

    #Returns the number of creatures in the stable
    def __len__(self):
        return len(self._creatures)

    #Returns "True" if a creature with that name is present in the stable
    def __contains__(self, name: str):
        for creature in self._creatures:
            if creature.name == name:
                return True
        return False

    #Iterates over all creatures
    def __iter__(self) -> Iterator[Creature]:
        return iter(self._creatures)

    #stable[creature.name] -> same as find()
    def __getitem__(self,name: str):
        return self.find(name)

    #Stable('{len(Stable)} creatures: ["creature1", "creature2","creature3",...]
    def __repr__(self):
        names = [creature.name for creature in self._creatures]
        return f"Stable:({len(self)} creatures: {names})"

    #add(creature: Creature) (add a creature; raise ValueError if a creature with the same name already exists)
    def add(self, creature: Creature):
        if creature.name in self:
            raise ValueError(
                f"The creature named {creature.name!r} is already in the stable.")
        else:
            self._creatures.append(creature)
            print(f"{mf.blue(creature.name)}", mf.green("has been added"),"to the stable.")

    #remove(name: str) (remove by name; raise KeyError if not found)
    def remove(self, name: str):

        creature = self.find(name)
        if creature.name not in self:
            raise KeyError(f"{creature.name!r} was not found in the stable.")
        else:
            self._creatures.remove(creature)
            print(f"{mf.blue(creature.name)}", mf.red("has been removed"),"to the stable.")

    #find(name: str) -> Creature (return the creature with that name; raise KeyError if not found)
    def find(self, name: str):
        for creature in self:
            if creature.name == name:
                return creature

        raise KeyError(f"No creature named {name!r} was found.")

