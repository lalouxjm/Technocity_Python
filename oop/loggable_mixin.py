class LoggableMixin:

    def log_mission(self):
        log = f"[LOG]<{self.name}>(<{self.species}>) departed on a mission - duration: <{self.mission_duration_days()}> days."
        self._mission_log.append(log)

    def print_log(self):
        print(self._mission_log)