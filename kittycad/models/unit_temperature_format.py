from enum import Enum


class UnitTemperatureFormat(str, Enum):
    KELVIN = 'kelvin'
    CELSIUS = 'celsius'
    FAHRENHEIT = 'fahrenheit'
    REAUMUR = 'reaumur'
    RANKINE = 'rankine'

    def __str__(self) -> str:
        return str(self.value)
