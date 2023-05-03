from enum import Enum


class UnitTemperatureFormat(str, Enum):
    """The valid types of temperature unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Kelvin> """  # noqa: E501
    KELVIN = "kelvin"
    """# <https://en.wikipedia.org/wiki/Celsius> """  # noqa: E501
    CELSIUS = "celsius"
    """# <https://en.wikipedia.org/wiki/Fahrenheit> """  # noqa: E501
    FAHRENHEIT = "fahrenheit"
    """# <https://en.wikipedia.org/wiki/R%C3%A9aumur_scale> """  # noqa: E501
    REAUMUR = "reaumur"
    """# <https://en.wikipedia.org/wiki/Rankine_scale> """  # noqa: E501
    RANKINE = "rankine"

    def __str__(self) -> str:
        return str(self.value)
