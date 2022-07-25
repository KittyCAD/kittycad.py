from enum import Enum


class UnitMagneticFieldStrengthFormat(str, Enum):
    TESLA = 'tesla'
    GAUSS = 'gauss'

    def __str__(self) -> str:
        return str(self.value)
