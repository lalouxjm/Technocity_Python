

class RoboticGuard:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def describe_abilities(self):
        return f"{self.name} patrols the perimeter and fires laser beams."

    @staticmethod
    def mission_duration_days():
        return 1

    def __str__(self):
        return f"{self.name} [Robotic Guard — model {self.model}]"