from enum import Enum


class UnitTemperature(str, Enum):
    """The valid types of temperature units."""  # noqa: E501

    """# Celsius <https://en.wikipedia.org/wiki/Celsius> """  # noqa: E501
    CELSIUS = "celsius"
    """# Fahrenheit <https://en.wikipedia.org/wiki/Fahrenheit> """  # noqa: E501
    FAHRENHEIT = "fahrenheit"
    """# Kelvin <https://en.wikipedia.org/wiki/Kelvin> """  # noqa: E501
    KELVIN = "kelvin"
    """# Rankine <https://en.wikipedia.org/wiki/Rankine_scale> """  # noqa: E501
    RANKINE = "rankine"

    def __str__(self) -> str:
        return str(self.value)
