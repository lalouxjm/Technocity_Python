from oop.dragon import Dragon
from oop.loggable_mixin import LoggableMixin


class LegendaryDragon(Dragon, LoggableMixin):
    def __init__(self, name: str, species, origin, power_level, element, title: str):
        super().__init__(name, species, origin, power_level, element)


        self._title = None
        self.title = title

        self._mission_log = []


    def __str__(self):
        base = super().__str__()
        return f'{self.title}, {base}'

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        is_a_string = isinstance(value, str)
        if not is_a_string:
            raise TypeError('Title must be a string')
        else:
            self._title = value

    def send_on_mission(self):
        super().send_on_mission()
        self.log_mission()

