from enum import Enum


class UnitAngleFormat(str, Enum):
    """The valid types of angle formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Radian> """  # noqa: E501
    RADIAN = "radian"
    """# <https://en.wikipedia.org/wiki/Degree_(angle)> """  # noqa: E501
    DEGREE = "degree"
    """# <https://en.wikipedia.org/wiki/Minute_and_second_of_arc> """  # noqa: E501
    ARCMINUTE = "arcminute"
    """# <https://en.wikipedia.org/wiki/Minute_and_second_of_arc> """  # noqa: E501
    ARCSECOND = "arcsecond"
    """# <https://en.wikipedia.org/wiki/Minute_and_second_of_arc#Symbols_and_abbreviations> """  # noqa: E501
    MILLIARCSECOND = "milliarcsecond"
    """# <https://en.wikipedia.org/wiki/Turn_(angle)> """  # noqa: E501
    TURN = "turn"
    """# <https://en.wikipedia.org/wiki/Gradian> """  # noqa: E501
    GRADIAN = "gradian"

    def __str__(self) -> str:
        return str(self.value)
