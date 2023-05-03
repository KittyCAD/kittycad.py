from enum import Enum


class UnitPowerFormat(str, Enum):
    """The valid types of power unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Watt> """  # noqa: E501
    WATT = "watt"
    """# <https://en.wikipedia.org/wiki/Horsepower> """  # noqa: E501
    HORSEPOWER = "horsepower"
    """# <https://en.wikipedia.org/wiki/Watt#Milliwatt> """  # noqa: E501
    MILLIWATT = "milliwatt"

    def __str__(self) -> str:
        return str(self.value)
