import kwargs

class LoggableMixin:

    def __init__(self, **kwargs):
        self.mission_log: list[str] = []
        super().__init__(**kwargs)

    def log_mission(self):
        log = (f"[LOG]<{self.name}>(<{self.species}>) departed on a mission "
               f"- duration: <{self.mission_duration_days()}> days.")
        self.mission_log.append(log)
        print(log)

    def print_log(self):
        print(self.mission_log)