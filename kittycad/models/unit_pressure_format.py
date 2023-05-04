from enum import Enum


class UnitPressureFormat(str, Enum):
    """The valid types of pressure unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Pascal_(unit)> """  # noqa: E501
    PASCAL = "pascal"
    """# <https://en.wikipedia.org/wiki/Bar_(unit)> """  # noqa: E501
    BAR = "bar"
    """# MilliBar <https://en.wikipedia.org/wiki/Bar_(unit)> """  # noqa: E501
    MBAR = "mbar"
    """# <https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)> """  # noqa: E501
    ATMOSPHERE = "atmosphere"
    """# psi - <https://en.wikipedia.org/wiki/Pound_per_square_inch> """  # noqa: E501
    POUNDS_PER_SQUARE_INCH = "pounds_per_square_inch"

    def __str__(self) -> str:
        return str(self.value)
