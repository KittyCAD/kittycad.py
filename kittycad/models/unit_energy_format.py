from enum import Enum


class UnitEnergyFormat(str, Enum):
    JOULE = 'joule'
    CALORIE = 'calorie'
    BRITISH_THERMAL_UNIT = 'british_thermal_unit'
    BRITISH_THERMAL_UNIT_ISO = 'british_thermal_unit_iso'
    BRITISH_THERMAL_UNIT59 = 'british_thermal_unit59'
    FOOT_POUND = 'foot_pound'

    def __str__(self) -> str:
        return str(self.value)
