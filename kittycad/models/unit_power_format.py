from enum import Enum


class UnitPowerFormat(str, Enum):
    WATT = 'watt'
    HORSEPOWER = 'horsepower'
    MILLIWATT = 'milliwatt'

    def __str__(self) -> str:
        return str(self.value)
