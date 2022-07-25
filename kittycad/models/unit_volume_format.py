from enum import Enum


class UnitVolumeFormat(str, Enum):
    CUBIC_METER = 'cubic_meter'
    CUBIC_MILLIMETER = 'cubic_millimeter'
    CUBIC_KILOMETER = 'cubic_kilometer'
    LITER = 'liter'
    CUBIC_FOOT = 'cubic_foot'
    CUBIC_YARD = 'cubic_yard'
    CUBIC_MILE = 'cubic_mile'

    def __str__(self) -> str:
        return str(self.value)
