from enum import Enum


class UnitAreaFormat(str, Enum):
    SQUARE_METER = 'square_meter'
    SQUARE_FOOT = 'square_foot'
    SQUARE_INCH = 'square_inch'
    SQUARE_MILE = 'square_mile'
    SQUARE_KILOMETER = 'square_kilometer'
    HECTARE = 'hectare'
    ACRE = 'acre'

    def __str__(self) -> str:
        return str(self.value)
