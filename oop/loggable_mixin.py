from oop.creature import Creature

class LoggableMixin(Creature):

    def __init__(self, name , species, origin, power_level):
        super().__init__(name, species, origin, power_level)

        self._mission_log = []

    def log_mission(self):
        self._mission_log.append(
            f"[LOG]<{self.name}>(<{self.species}>) departed on a mission "
            f"- duration: <{self.mission_duration_days()}> days."
        )

    def mission_duration_days(self) -> int:
        ...
    def describe_abilities(self):
        ...