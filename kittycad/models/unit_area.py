from enum import Enum


class UnitArea(str, Enum):
    """The valid types of area units."""  # noqa: E501

    """# Square centimeters <https://en.wikipedia.org/wiki/Square_centimeter> """  # noqa: E501
    CM2 = "cm2"
    """# Square decimeters <https://en.wikipedia.org/wiki/Square_decimeter> """  # noqa: E501
    DM2 = "dm2"
    """# Square feet <https://en.wikipedia.org/wiki/Square_foot> """  # noqa: E501
    FT2 = "ft2"
    """# Square inches <https://en.wikipedia.org/wiki/Square_inch> """  # noqa: E501
    IN2 = "in2"
    """# Square kilometers <https://en.wikipedia.org/wiki/Square_kilometer> """  # noqa: E501
    KM2 = "km2"
    """# Square meters <https://en.wikipedia.org/wiki/Square_meter> """  # noqa: E501
    M2 = "m2"
    """# Square millimeters <https://en.wikipedia.org/wiki/Square_millimeter> """  # noqa: E501
    MM2 = "mm2"
    """# Square yards <https://en.wikipedia.org/wiki/Square_mile> """  # noqa: E501
    YD2 = "yd2"

    def __str__(self) -> str:
        return str(self.value)
