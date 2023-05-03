from enum import Enum


class UnitEnergyFormat(str, Enum):
    """The valid types of energy unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Joule> """  # noqa: E501
    JOULE = "joule"
    """# <https://en.wikipedia.org/wiki/Calorie> """  # noqa: E501
    CALORIE = "calorie"
    """# <https://en.wikipedia.org/wiki/Kilowatt-hour> """  # noqa: E501
    KILOWATT_HOUR = "kilowatt_hour"
    """# <https://en.wikipedia.org/wiki/Kilowatt-hour> """  # noqa: E501
    WATT_HOUR = "watt_hour"
    """# <https://en.wikipedia.org/wiki/British_thermal_unit> """  # noqa: E501
    BRITISH_THERMAL_UNIT = "british_thermal_unit"
    """# <https://en.wikipedia.org/wiki/Therm#Definitions> """  # noqa: E501
    BRITISH_THERMAL_UNIT_ISO = "british_thermal_unit_iso"
    """# <https://en.wikipedia.org/wiki/Therm#Definitions> """  # noqa: E501
    BRITISH_THERMAL_UNIT59 = "british_thermal_unit59"
    """# <https://en.wikipedia.org/wiki/Therm> """  # noqa: E501
    THERM = "therm"
    """# <https://en.wikipedia.org/wiki/Foot-pound_(energy)> """  # noqa: E501
    FOOT_POUND = "foot_pound"

    def __str__(self) -> str:
        return str(self.value)
