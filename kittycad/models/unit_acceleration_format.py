from enum import Enum


class UnitAccelerationFormat(str, Enum):
    METERS_PER_SECOND_SQUARED = 'meters_per_second_squared'
    FEET_PER_SECOND_SQUARED = 'feet_per_second_squared'
    STANDARD_GRAVITY = 'standard_gravity'

    def __str__(self) -> str:
        return str(self.value)
