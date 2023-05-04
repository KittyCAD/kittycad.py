from enum import Enum


class UnitAreaFormat(str, Enum):
    """The valid types of area unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Square_metre> """  # noqa: E501
    SQUARE_METER = "square_meter"
    """# <https://en.wikipedia.org/wiki/Square_foot> """  # noqa: E501
    SQUARE_FOOT = "square_foot"
    """# <https://en.wikipedia.org/wiki/Square_inch> """  # noqa: E501
    SQUARE_INCH = "square_inch"
    """# <https://en.wikipedia.org/wiki/Square_mile> """  # noqa: E501
    SQUARE_MILE = "square_mile"
    """# <https://en.wikipedia.org/wiki/Square_kilometre> """  # noqa: E501
    SQUARE_KILOMETER = "square_kilometer"
    """# <https://en.wikipedia.org/wiki/Hectare> """  # noqa: E501
    HECTARE = "hectare"
    """# <https://en.wikipedia.org/wiki/Acre> """  # noqa: E501
    ACRE = "acre"

    def __str__(self) -> str:
        return str(self.value)
