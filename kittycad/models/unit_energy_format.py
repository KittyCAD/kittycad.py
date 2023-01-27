from enum import Enum


class UnitEnergyFormat(str, Enum):
    JOULE = 'joule'
    CALORIE = 'calorie'
    KILOWATT_HOUR = 'kilowatt_hour'
    WATT_HOUR = 'watt_hour'
    BRITISH_THERMAL_UNIT = 'british_thermal_unit'
    BRITISH_THERMAL_UNIT_ISO = 'british_thermal_unit_iso'
    BRITISH_THERMAL_UNIT59 = 'british_thermal_unit59'
    THERM = 'therm'
    FOOT_POUND = 'foot_pound'

    def __str__(self) -> str:
        return str(self.value)
