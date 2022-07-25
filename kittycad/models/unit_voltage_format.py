from enum import Enum


class UnitVoltageFormat(str, Enum):
    VOLT = 'volt'
    STATVOLT = 'statvolt'
    ABVOLT = 'abvolt'

    def __str__(self) -> str:
        return str(self.value)
