from datetime import date

import my_func as f
from oop.creature import Creature
from oop.dragon import Dragon
from oop.basilisk import Basilisk
from oop.griffin import Griffin
from oop.mission_records import MissionRecord
from oop.phoenix import Phoenix
from oop.robotic_guard import RoboticGuard
from oop.scroll_archive import ScrollArchive
from oop.stable import Stable
from oop.unicorn import Unicorn
from oop.legendary_dragon import LegendaryDragon



c1 = Dragon(name="Glacius", species="Dragon", origin="Nordic Mountains", power_level=95, element="Ice")
c2 = Unicorn(name="Rainbow", species="Unicorn", origin="Mist Forest", power_level=51)
c3 = Phoenix(name="Marco", species="Phoenix", origin="Wild Plains", power_level=6)
c4 = Griffin.add_from_dict({'name':"Diamond", 'species':"Griffin", 'origin':"Bowieland", 'power_level': 10})
c5 = Basilisk.add_from_string("RazorSting,Basilisk,Poison Marsh,32")

c6 = LegendaryDragon(name="Ignis", species="Dragon", origin="Volcanic Depths", power_level=99, element="Fire", title="The Destroyer")

stable = Stable()

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
stable.add(c1)
stable.add(c2)
stable.add(c3)
stable.add(c4)
stable.add(c5)
stable.add(c6)
stable.remove(c4.name)
stable.remove("RazorSting")
print(f"There are {len(stable)} creatures in the stable")
print(stable)
print(f"Is {c6.name} in the stable? ", c6.name in stable)#True
print(f"Is {c4.name} in the stable? ","Diamond" in stable)#False
print(stable["Glacius"])
for creature in stable:
    print(creature.describe_abilities())
print(stable)
print(stable.find("Ignis"))
f.sep()
r1 = MissionRecord("Glacius", "Frozen Peaks", date(2025, 1, 10), 14)
r2 = MissionRecord("Glacius", "Northern Pass", date(2025, 1, 10), 7)
r3 = MissionRecord("Ignis", "Ashlands", date(2025, 1, 10), 7)
print(r1 == r2)         # True
print(hash(r1) == hash(r2))  # True
f.sep()
with ScrollArchive("stable_log.txt") as scroll:
    scroll.write_departure(r1)
    scroll.write_departure(r2)
    scroll.write_return("Glacius")
f.sep()
try:
    with ScrollArchive("stable_log.txt") as scroll:
        scroll.write_departure(r1)
        raise ValueError("Simulated crash mid-mission!")
        scroll.write_departure(record2)  #never reached
except ValueError as error:
    print(f"ValueError still propagated: {error}")