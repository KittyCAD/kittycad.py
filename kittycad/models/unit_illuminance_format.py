from enum import Enum


class UnitIlluminanceFormat(str, Enum):
    """The valid types of illuminance unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Lux> """  # noqa: E501
    LUX = "lux"
    """# <https://en.wikipedia.org/wiki/Foot-candle> """  # noqa: E501
    FOOTCANDLE = "footcandle"
    """# <https://en.wikipedia.org/wiki/Lumen_(unit)> """  # noqa: E501
    LUMENS_PER_SQUARE_INCH = "lumens_per_square_inch"
    """# <https://en.wikipedia.org/wiki/Phot> """  # noqa: E501
    PHOT = "phot"

    def __str__(self) -> str:
        return str(self.value)
