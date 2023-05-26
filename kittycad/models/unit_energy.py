from enum import Enum


class UnitEnergy(str, Enum):
    """The valid types of energy units."""  # noqa: E501

    """# British Thermal Unit (BTU) <https://en.wikipedia.org/wiki/British_thermal_unit> """  # noqa: E501
    BTU = "btu"
    """# Electron Volts (eV) <https://en.wikipedia.org/wiki/Electronvolt> """  # noqa: E501
    ELECTRONVOLTS = "electronvolts"
    """# Joules (or watt-seconds) <https://en.wikipedia.org/wiki/Joule> """  # noqa: E501
    JOULES = "joules"
    """# Kilocalories (often just called calories) <https://en.wikipedia.org/wiki/Kilocalorie> """  # noqa: E501
    KILOCALORIES = "kilocalories"
    """# Kilowatt hours (kWh) <https://en.wikipedia.org/wiki/Kilowatt-hour> """  # noqa: E501
    KILOWATT_HOURS = "kilowatt_hours"
    """# Watt hours (Wh) <https://en.wikipedia.org/wiki/Kilowatt-hour> """  # noqa: E501
    WATT_HOURS = "watt_hours"

    def __str__(self) -> str:
        return str(self.value)
