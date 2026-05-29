from oop.dragon import Dragon
from oop.loggable_mixin import LoggableMixin
import my_func as mf


class LegendaryDragon(LoggableMixin, Dragon):
    def __init__(self, name: str, origin, power_level, element, title: str):
        super().__init__(name=name, origin=origin, power_level=power_level, element=element)

        self._title = None
        self.title = title

        self._mission_log = []

    def __str__(self):
        status = mf.green("In Stable") if self._in_stable else mf.red("On Mission")
        return f"{mf.blue(self._name, ", ", self.title)} - LvL {self._power_level} {mf.yellow("<[",self.element,"]", self._species, ">")} (origin: {self._origin!r}) [{status}]"

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError('Title must be a string')
        else:
            self._title = value

    def send_on_mission(self):
        super().send_on_mission()
        self.log_mission()

