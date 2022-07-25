from enum import Enum


class UnitPressureFormat(str, Enum):
    PASCAL = 'pascal'
    BAR = 'bar'
    MBAR = 'mbar'
    ATMOSPHERE = 'atmosphere'
    POUNDS_PER_SQUARE_INCH = 'pounds_per_square_inch'

    def __str__(self) -> str:
        return str(self.value)
