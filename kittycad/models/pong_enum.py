from enum import Enum


class PongEnum(str, Enum):
    PONG = 'pong'

    def __str__(self) -> str:
        return str(self.value)
