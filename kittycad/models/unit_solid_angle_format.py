from enum import Enum


class UnitSolidAngleFormat(str, Enum):
    STERADIAN = 'steradian'
    DEGREE_SQUARED = 'degree_squared'
    SPAT = 'spat'

    def __str__(self) -> str:
        return str(self.value)
