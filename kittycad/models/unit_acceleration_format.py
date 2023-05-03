from enum import Enum


class UnitAccelerationFormat(str, Enum):
    """The valid types of acceleration unit formats."""  # noqa: E501

    """# Acceleration in m/s^2 unit form """  # noqa: E501
    METERS_PER_SECOND_SQUARED = "meters_per_second_squared"
    """# Acceleration in ft/s^2 unit form """  # noqa: E501
    FEET_PER_SECOND_SQUARED = "feet_per_second_squared"
    """# Acceleration in standard gravity (g) unit form (aka where 9.80665 m/s^2 is the base unit). <https://en.wikipedia.org/wiki/Standard_gravity> """  # noqa: E501
    STANDARD_GRAVITY = "standard_gravity"

    def __str__(self) -> str:
        return str(self.value)
