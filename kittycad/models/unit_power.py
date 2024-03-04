from enum import Enum


class UnitPower(str, Enum):
    """The valid types of power units."""  # noqa: E501

    """# British thermal units (BTU) per minute <https://en.wikipedia.org/wiki/British_thermal_unit> """  # noqa: E501
    BTU_PER_MINUTE = "btu_per_minute"
    """# Horsepower (hp) <https://en.wikipedia.org/wiki/Horsepower> """  # noqa: E501
    HORSEPOWER = "horsepower"
    """# Kilowatts <https://en.wikipedia.org/wiki/Kilowatt> """  # noqa: E501
    KILOWATTS = "kilowatts"
    """# Metric horsepower (PS) <https://en.wikipedia.org/wiki/Horsepower#Metric_horsepower> """  # noqa: E501
    METRIC_HORSEPOWER = "metric_horsepower"
    """# Microwatts <https://en.wikipedia.org/wiki/Microwatt> """  # noqa: E501
    MICROWATTS = "microwatts"
    """# Millwatts <https://en.wikipedia.org/wiki/Milliwatt> """  # noqa: E501
    MILLIWATTS = "milliwatts"
    """# Watts <https://en.wikipedia.org/wiki/Watt> """  # noqa: E501
    WATTS = "watts"

    def __str__(self) -> str:
        return str(self.value)
