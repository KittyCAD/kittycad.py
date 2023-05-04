from enum import Enum


class UnitTimeFormat(str, Enum):
    """The valid types of time unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Second> """  # noqa: E501
    SECOND = "second"
    """# <https://en.wikipedia.org/wiki/Minute> """  # noqa: E501
    MINUTE = "minute"
    """# <https://en.wikipedia.org/wiki/Hour> """  # noqa: E501
    HOUR = "hour"
    """# <https://en.wikipedia.org/wiki/Day> """  # noqa: E501
    DAY = "day"
    """# <https://en.wikipedia.org/wiki/Week> """  # noqa: E501
    WEEK = "week"
    """# <https://en.wikipedia.org/wiki/Year> """  # noqa: E501
    YEAR = "year"
    """# <https://en.wikipedia.org/wiki/Julian_year> """  # noqa: E501
    JULIAN_YEAR = "julian_year"
    """# <https://en.wikipedia.org/wiki/Gregorian_calendar> """  # noqa: E501
    GREGORIAN_YEAR = "gregorian_year"

    def __str__(self) -> str:
        return str(self.value)
