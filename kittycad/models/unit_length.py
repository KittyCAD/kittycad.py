from enum import Enum


class UnitLength(str, Enum):
    """The valid types of length units."""  # noqa: E501

    """# Centimetres <https://en.wikipedia.org/wiki/Centimetre> """  # noqa: E501
    CENTIMETRES = "centimetres"
    """# Decimetres <https://en.wikipedia.org/wiki/Decimetre> """  # noqa: E501
    DECIMETRES = "decimetres"
    """# Feet <https://en.wikipedia.org/wiki/Foot_(unit)> """  # noqa: E501
    FEET = "feet"
    """# Furlongs <https://en.wikipedia.org/wiki/Furlong> """  # noqa: E501
    FURLONGS = "furlongs"
    """# Hectometres <https://en.wikipedia.org/wiki/Hectometre> """  # noqa: E501
    HECTOMETRES = "hectometres"
    """# Inches <https://en.wikipedia.org/wiki/Inch> """  # noqa: E501
    INCHES = "inches"
    """# Kilometres <https://en.wikipedia.org/wiki/Kilometre> """  # noqa: E501
    KILOMETRES = "kilometres"
    """# Metres <https://en.wikipedia.org/wiki/Metre> """  # noqa: E501
    METRES = "metres"
    """# Micrometres <https://en.wikipedia.org/wiki/Micrometre> """  # noqa: E501
    MICROMETRES = "micrometres"
    """# Miles <https://en.wikipedia.org/wiki/Mile> """  # noqa: E501
    MILES = "miles"
    """# Millimetres <https://en.wikipedia.org/wiki/Millimetre> """  # noqa: E501
    MILLIMETRES = "millimetres"
    """# Nanometres <https://en.wikipedia.org/wiki/Nanometre> """  # noqa: E501
    NANOMETRES = "nanometres"
    """# Yards <https://en.wikipedia.org/wiki/Yard> """  # noqa: E501
    YARDS = "yards"

    def __str__(self) -> str:
        return str(self.value)
