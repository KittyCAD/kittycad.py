from enum import Enum


class UnitIlluminanceFormat(str, Enum):
    LUX = 'lux'
    FOOTCANDLE = 'footcandle'
    LUMENS_PER_SQUARE_INCH = 'lumens_per_square_inch'
    PHOT = 'phot'

    def __str__(self) -> str:
        return str(self.value)
