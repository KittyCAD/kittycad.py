from enum import Enum


class UnitVoltageFormat(str, Enum):
    """The valid types of voltage unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Volt> """  # noqa: E501
    VOLT = "volt"
    """# <https://en.wikipedia.org/wiki/Statvolt> """  # noqa: E501
    STATVOLT = "statvolt"
    """# <https://en.wikipedia.org/wiki/Abvolt> """  # noqa: E501
    ABVOLT = "abvolt"

    def __str__(self) -> str:
        return str(self.value)
