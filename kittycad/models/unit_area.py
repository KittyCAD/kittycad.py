from enum import Enum


class UnitArea(str, Enum):
    """The valid types of area units."""  # noqa: E501

    """# Square centimetres <https://en.wikipedia.org/wiki/Square_centimetre> """  # noqa: E501
    CM2 = "cm2"
    """# Square decimetres <https://en.wikipedia.org/wiki/Square_decimetre> """  # noqa: E501
    DM2 = "dm2"
    """# Square feet <https://en.wikipedia.org/wiki/Square_foot> """  # noqa: E501
    FT2 = "ft2"
    """# Square inches <https://en.wikipedia.org/wiki/Square_inch> """  # noqa: E501
    IN2 = "in2"
    """# Square kilometres <https://en.wikipedia.org/wiki/Square_kilometre> """  # noqa: E501
    KM2 = "km2"
    """# Square metres <https://en.wikipedia.org/wiki/Square_metre> """  # noqa: E501
    M2 = "m2"
    """# Square millimetres <https://en.wikipedia.org/wiki/Square_millimetre> """  # noqa: E501
    MM2 = "mm2"
    """# Square yards <https://en.wikipedia.org/wiki/Square_mile> """  # noqa: E501
    YD2 = "yd2"

    def __str__(self) -> str:
        return str(self.value)
