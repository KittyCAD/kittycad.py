from enum import Enum


class UnitLength(str, Enum):
    """The valid types of length units."""  # noqa: E501

    """# Centimeters <https://en.wikipedia.org/wiki/Centimeter> """  # noqa: E501
    CM = "cm"
    """# Feet <https://en.wikipedia.org/wiki/Foot_(unit)> """  # noqa: E501
    FT = "ft"
    """# Inches <https://en.wikipedia.org/wiki/Inch> """  # noqa: E501
    IN = "in"
    """# Meters <https://en.wikipedia.org/wiki/Meter> """  # noqa: E501
    M = "m"
    """# Millimeters <https://en.wikipedia.org/wiki/Millimeter> """  # noqa: E501
    MM = "mm"
    """# Yards <https://en.wikipedia.org/wiki/Yard> """  # noqa: E501
    YD = "yd"

    def __str__(self) -> str:
        return str(self.value)
