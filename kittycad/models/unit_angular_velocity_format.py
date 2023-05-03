from enum import Enum


class UnitAngularVelocityFormat(str, Enum):
    """The valid types of angular velocity unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Radian_per_second> """  # noqa: E501
    RADIANS_PER_SECOND = "radians_per_second"
    """# <https://en.wikipedia.org/wiki/Rotational_speed> """  # noqa: E501
    DEGREES_PER_SECOND = "degrees_per_second"
    """# <https://en.wikipedia.org/wiki/Revolutions_per_minute> """  # noqa: E501
    REVOLUTIONS_PER_MINUTE = "revolutions_per_minute"
    """# <https://en.wikipedia.org/wiki/Minute_and_second_of_arc#Symbols_and_abbreviations> """  # noqa: E501
    MILLIARCSECONDS_PER_YEAR = "milliarcseconds_per_year"

    def __str__(self) -> str:
        return str(self.value)
