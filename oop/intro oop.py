from oop.creature import Creature
from oop.dragon import Dragon
from oop.basilisk import Basilisk
from oop.griffin import Griffin
from oop.phoenix import Phoenix
from oop.unicorn import Unicorn


c1 = Dragon("Glacius", species="Dragon", origin="Nordic Mountains", power_level=95, element="Ice")
c2 = Unicorn("Rainbow", species="Unicorn", origin="Mist Forest", power_level=51)
c3 = Phoenix("Marco", species="Phoenix", origin="Wild Plains", power_level=6)
c4 = Griffin.add_from_dict({'name':"Diamond", 'species':"Griffin", 'origin':"Bowieland", 'power_level': 10})
c5 = Basilisk.add_from_string("RazorSting,Basilisk,Poison Marsh,32")

Creature.get_total_creatures()
Dragon.get_total_creatures()

print("+++===+++")
c1.send_to_field()
print("+++===+++")
c2.send_to_field()
print("+++===+++")
print(c3)
print("+++===+++")
c4.send_to_field()
print("+++===+++")
c5.send_to_field()
print("+++===+++")
c1.return_from_mission()
print(c1)
print("+++===+++")
