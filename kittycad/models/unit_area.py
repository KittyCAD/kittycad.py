from enum import Enum


class UnitArea(str, Enum):
    """The valid types of area units."""  # noqa: E501

    """# Acres <https://en.wikipedia.org/wiki/Acre> """  # noqa: E501
    ACRES = "acres"
    """# Hectares <https://en.wikipedia.org/wiki/Hectare> """  # noqa: E501
    HECTARES = "hectares"
    """# Square centimetres <https://en.wikipedia.org/wiki/Square_centimetre> """  # noqa: E501
    SQUARE_CENTIMETRES = "square_centimetres"
    """# Square decimetres <https://en.wikipedia.org/wiki/Square_decimetre> """  # noqa: E501
    SQUARE_DECIMETRES = "square_decimetres"
    """# Square feet <https://en.wikipedia.org/wiki/Square_foot> """  # noqa: E501
    SQUARE_FEET = "square_feet"
    """# Square hectometres <https://en.wikipedia.org/wiki/Square_hectometre> """  # noqa: E501
    SQUARE_HECTOMETRES = "square_hectometres"
    """# Square inches <https://en.wikipedia.org/wiki/Square_inch> """  # noqa: E501
    SQUARE_INCHES = "square_inches"
    """# Square kilometres <https://en.wikipedia.org/wiki/Square_kilometre> """  # noqa: E501
    SQUARE_KILOMETRES = "square_kilometres"
    """# Square metres <https://en.wikipedia.org/wiki/Square_metre> """  # noqa: E501
    SQUARE_METRES = "square_metres"
    """# Square micrometres <https://en.wikipedia.org/wiki/Square_micrometre> """  # noqa: E501
    SQUARE_MICROMETRES = "square_micrometres"
    """# Square miles <https://en.wikipedia.org/wiki/Square_mile> """  # noqa: E501
    SQUARE_MILES = "square_miles"
    """# Square millimetres <https://en.wikipedia.org/wiki/Square_millimetre> """  # noqa: E501
    SQUARE_MILLIMETRES = "square_millimetres"
    """# Square nanometres <https://en.wikipedia.org/wiki/Square_nanometre> """  # noqa: E501
    SQUARE_NANOMETRES = "square_nanometres"
    """# Square yards <https://en.wikipedia.org/wiki/Square_mile> """  # noqa: E501
    SQUARE_YARDS = "square_yards"

    def __str__(self) -> str:
        return str(self.value)
