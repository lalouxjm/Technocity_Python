import my_func as f
from oop.creature import Creature
from oop.dragon import Dragon
from oop.basilisk import Basilisk
from oop.griffin import Griffin
from oop.phoenix import Phoenix
from oop.robotic_guard import RoboticGuard
from oop.unicorn import Unicorn
from oop.legendary_dragon import LegendaryDragon



c1 = Dragon(name="Glacius", species="Dragon", origin="Nordic Mountains", power_level=95, element="Ice")
c2 = Unicorn(name="Rainbow", species="Unicorn", origin="Mist Forest", power_level=51)
c3 = Phoenix(name="Marco", species="Phoenix", origin="Wild Plains", power_level=6)
c4 = Griffin.add_from_dict({'name':"Diamond", 'species':"Griffin", 'origin':"Bowieland", 'power_level': 10})
c5 = Basilisk.add_from_string("RazorSting,Basilisk,Poison Marsh,32")

c6 = LegendaryDragon(name="Ignis", species="Dragon", origin="Volcanic Depths", power_level=99, element="Fire", title="The Destroyer")

Creature.get_total_creatures()
Dragon.get_total_creatures()

f.sep()
c1.send_to_field()
c1.return_from_mission()
f.sep()
c2.send_to_field()
c2.return_from_mission()
f.sep()
print(c3)
c3.fly()
f.sep()
c4.send_to_field()
f.sep()
c5.send_to_field()
f.sep()
print(c1)
c1.return_from_mission()
f.sep()
c6.send_to_field()
c6.return_from_mission()
f.sep()
print(LegendaryDragon.__mro__)
f.sep()
r1 = RoboticGuard("Shadow Sentinel", "MK.III")
print(r1)
f.sep()
creature_list = [c1, c2, c3, c4, c5, c6, r1]
Creature.end_of_day_report(creature_list)
f.sep()


