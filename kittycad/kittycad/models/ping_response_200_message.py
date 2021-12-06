from enum import Enum


class PingResponse200Message(str, Enum):
    PONG = "pong"

    def __str__(self) -> str:
        return str(self.value)
