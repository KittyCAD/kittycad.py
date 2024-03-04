from enum import Enum


class UnitTorque(str, Enum):
    """The valid types of torque units."""  # noqa: E501

    """# Newton metres <https://en.wikipedia.org/wiki/Newton_metre> """  # noqa: E501
    NEWTON_METRES = "newton_metres"
    """# Pound foot <https://en.wikipedia.org/wiki/Pound-foot_(torque)> """  # noqa: E501
    POUND_FOOT = "pound_foot"

    def __str__(self) -> str:
        return str(self.value)
