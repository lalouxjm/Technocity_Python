from typing import Protocol


class MissionNotifier(Protocol):
    @staticmethod
    def notify(message: str) -> None:
        ...


class ScrollNotifier:
    @staticmethod
    def notify(message: str) -> None:
        print(f"📜 [SCROLL] {message}")


class MirrorNotifier:
    @staticmethod
    def notify(message: str) -> None:
        filepath = "mirror_log.txt"
        with open(filepath, "a") as file:
            file.write(f" [MIRROR] {message}")
        print("🪞 Notified in mirror")


class SilentNotifier:
    @staticmethod
    def notify(message: str) -> None:
        print("The raven failed to deliver the message")


class MissionDispatcher:
    def __init__(self, notifier: MissionNotifier) -> None:
        self._notifier = notifier

    def dispatch(self, creature_name: str, destination: str) -> None:
        self._notifier.notify(f"{creature_name} dispatched to {destination}")