from enum import Enum


class UnitAngleFormat(str, Enum):
    RADIAN = 'radian'
    DEGREE = 'degree'
    ARCMINUTE = 'arcminute'
    ARCSECOND = 'arcsecond'
    MILLIARCSECOND = 'milliarcsecond'
    TURN = 'turn'
    GRADIAN = 'gradian'

    def __str__(self) -> str:
        return str(self.value)
