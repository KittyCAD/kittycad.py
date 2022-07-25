from enum import Enum


class UnitDataFormat(str, Enum):
    BYTE = 'byte'
    EXABYTE = 'exabyte'
    BIT = 'bit'
    EXABIT = 'exabit'

    def __str__(self) -> str:
        return str(self.value)
