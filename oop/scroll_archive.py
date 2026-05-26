from oop.mission_records import MissionRecord

class ScrollArchive:
    def __init__(self, filepath:str) -> None:
        self.filepath = filepath

    def __enter__(self) -> "ScrollArchive":
        self._file = open(self.filepath, "a")
        print(f"📜 Scroll opened: {self.filepath}")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("📜 Scroll sealed.")
        else:
            print(f"⚠️  Scroll sealed after error: {exc_val}")

        return False


    def write_departure(self, record: MissionRecord):
        print(f"DEPARTURE: {record}")
        self._file.write(f"DEPARTURE: {record}\n")

    def write_return(self, creature_name: str):
        print(f"RETURN: {creature_name}")
        self._file.write(f"RETURN: {creature_name}\n")



