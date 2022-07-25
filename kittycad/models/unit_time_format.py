from enum import Enum


class UnitTimeFormat(str, Enum):
    SECOND = 'second'
    MINUTE = 'minute'
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    YEAR = 'year'
    JULIAN_YEAR = 'julian_year'
    GREGORIAN_YEAR = 'gregorian_year'

    def __str__(self) -> str:
        return str(self.value)
