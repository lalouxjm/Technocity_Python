import my_func as f
from oop.creature import Creature
from oop.dragon import Dragon
from oop.basilisk import Basilisk
from oop.griffin import Griffin
from oop.phoenix import Phoenix
from oop.unicorn import Unicorn
from oop.legendary_dragon import LegendaryDragon



c1 = Dragon(name="Glacius", species="Dragon", origin="Nordic Mountains", power_level=95, element="Ice")
c2 = Unicorn(name="Rainbow", species="Unicorn", origin="Mist Forest", power_level=51)
c3 = Phoenix(name="Marco", species="Phoenix", origin="Wild Plains", power_level=6)
c4 = Griffin.add_from_dict({'name':"Diamond", 'species':"Griffin", 'origin':"Bowieland", 'power_level': 10})
c5 = Basilisk.add_from_string("RazorSting,Basilisk,Poison Marsh,32")

c6 = LegendaryDragon(name="Ignis the Legendary Dragon", species="Legendary Dragon", origin="Volcanic Depths", power_level=99, element="Fire", title="The Destroyer")

Creature.get_total_creatures()
Dragon.get_total_creatures()

f.sep()
c1.send_to_field()
f.sep()
c2.send_to_field()
f.sep()
print(c3)
f.sep()
c4.send_to_field()
f.sep()
c5.send_to_field()
f.sep()
print(c1)
c1.return_from_mission()
f.sep()
c6.send_to_field()
f.sep()
print(LegendaryDragon.__mro__)
f.sep()


