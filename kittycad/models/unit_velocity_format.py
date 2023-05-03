from enum import Enum


class UnitVelocityFormat(str, Enum):
    """The valid types of velocity unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Metre_per_second> """  # noqa: E501
    METERS_PER_SECOND = "meters_per_second"
    """# <https://en.wikipedia.org/wiki/Foot_per_second> """  # noqa: E501
    FEET_PER_SECOND = "feet_per_second"
    """# <https://en.wikipedia.org/wiki/Miles_per_hour> """  # noqa: E501
    MILES_PER_HOUR = "miles_per_hour"
    """# <https://en.wikipedia.org/wiki/Kilometres_per_hour> """  # noqa: E501
    KILOMETERS_PER_HOUR = "kilometers_per_hour"
    """# <https://en.wikipedia.org/wiki/Knot_(unit)> """  # noqa: E501
    KNOT = "knot"

    def __str__(self) -> str:
        return str(self.value)
