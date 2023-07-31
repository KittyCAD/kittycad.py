from enum import Enum


class UnitLength(str, Enum):
    """The valid types of length units."""  # noqa: E501

    """# Centimetres <https://en.wikipedia.org/wiki/Centimetre> """  # noqa: E501
    CM = "cm"
    """# Feet <https://en.wikipedia.org/wiki/Foot_(unit)> """  # noqa: E501
    FT = "ft"
    """# Inches <https://en.wikipedia.org/wiki/Inch> """  # noqa: E501
    IN = "in"
    """# Metres <https://en.wikipedia.org/wiki/Metre> """  # noqa: E501
    M = "m"
    """# Millimetres <https://en.wikipedia.org/wiki/Millimetre> """  # noqa: E501
    MM = "mm"
    """# Yards <https://en.wikipedia.org/wiki/Yard> """  # noqa: E501
    YD = "yd"

    def __str__(self) -> str:
        return str(self.value)
