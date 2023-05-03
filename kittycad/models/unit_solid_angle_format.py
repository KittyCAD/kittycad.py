from enum import Enum


class UnitSolidAngleFormat(str, Enum):
    """The valid types of solid angle unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Steradian> """  # noqa: E501
    STERADIAN = "steradian"
    """# <https://en.wikipedia.org/wiki/Square_degree> """  # noqa: E501
    DEGREE_SQUARED = "degree_squared"
    """# <https://en.wikipedia.org/wiki/Spat_(angular_unit)> """  # noqa: E501
    SPAT = "spat"

    def __str__(self) -> str:
        return str(self.value)
