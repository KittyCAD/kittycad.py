from enum import Enum


class UnitRadiationFormat(str, Enum):
    GRAY = 'gray'
    SIEVERT = 'sievert'
    RAD = 'rad'

    def __str__(self) -> str:
        return str(self.value)
