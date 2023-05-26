from enum import Enum


class UnitAngle(str, Enum):
    """The valid types of angle formats."""  # noqa: E501

    """# Degrees <https://en.wikipedia.org/wiki/Degree_(angle)> """  # noqa: E501
    DEGREES = "degrees"
    """# Radians <https://en.wikipedia.org/wiki/Radian> """  # noqa: E501
    RADIANS = "radians"

    def __str__(self) -> str:
        return str(self.value)
