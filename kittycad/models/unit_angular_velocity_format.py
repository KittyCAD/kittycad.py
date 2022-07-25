from enum import Enum


class UnitAngularVelocityFormat(str, Enum):
    RADIANS_PER_SECOND = 'radians_per_second'
    DEGREES_PER_SECOND = 'degrees_per_second'
    REVOLUTIONS_PER_MINUTE = 'revolutions_per_minute'
    MILLIARCSECONDS_PER_YEAR = 'milliarcseconds_per_year'

    def __str__(self) -> str:
        return str(self.value)
