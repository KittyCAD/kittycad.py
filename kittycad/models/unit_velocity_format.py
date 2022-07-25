from enum import Enum


class UnitVelocityFormat(str, Enum):
    METERS_PER_SECOND = 'meters_per_second'
    FEET_PER_SECOND = 'feet_per_second'
    MILES_PER_HOUR = 'miles_per_hour'
    KILOMETERS_PER_HOUR = 'kilometers_per_hour'
    KNOT = 'knot'

    def __str__(self) -> str:
        return str(self.value)
