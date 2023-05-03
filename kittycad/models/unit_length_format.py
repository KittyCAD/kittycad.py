from enum import Enum


class UnitLengthFormat(str, Enum):
    """The valid types of length unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Metre> """  # noqa: E501
    METER = "meter"
    """# <https://en.wikipedia.org/wiki/Millimetre> """  # noqa: E501
    MILLIMETER = "millimeter"
    """# <https://en.wikipedia.org/wiki/Centimetre> """  # noqa: E501
    CENTIMETER = "centimeter"
    """# <https://en.wikipedia.org/wiki/Kilometre> """  # noqa: E501
    KILOMETER = "kilometer"
    """# <https://en.wikipedia.org/wiki/Foot_(unit)> """  # noqa: E501
    FOOT = "foot"
    """# <https://en.wikipedia.org/wiki/Thousandth_of_an_inch> """  # noqa: E501
    MIL = "mil"
    """# <https://en.wikipedia.org/wiki/Inch> """  # noqa: E501
    INCH = "inch"
    """# <https://en.wikipedia.org/wiki/Mile> """  # noqa: E501
    MILE = "mile"
    """# <https://en.wikipedia.org/wiki/Nautical_mile> """  # noqa: E501
    NAUTICAL_MILE = "nautical_mile"
    """# <https://en.wikipedia.org/wiki/Astronomical_unit> """  # noqa: E501
    ASTRONOMICAL_UNIT = "astronomical_unit"
    """# <https://en.wikipedia.org/wiki/Light-year> """  # noqa: E501
    LIGHTYEAR = "lightyear"
    """# <https://en.wikipedia.org/wiki/Parsec> """  # noqa: E501
    PARSEC = "parsec"
    """# <https://en.wikipedia.org/wiki/Angstrom> """  # noqa: E501
    ANGSTROM = "angstrom"
    """# <https://en.wikipedia.org/wiki/Cubit> """  # noqa: E501
    CUBIT = "cubit"
    """# <https://en.wikipedia.org/wiki/Fathom> """  # noqa: E501
    FATHOM = "fathom"
    """# <https://en.wikipedia.org/wiki/Chain_(unit)> """  # noqa: E501
    CHAIN = "chain"
    """# <https://en.wikipedia.org/wiki/Furlong> """  # noqa: E501
    FURLONG = "furlong"
    """# <https://en.wikipedia.org/wiki/Hand_(unit)> """  # noqa: E501
    HAND = "hand"
    """# <https://en.wikipedia.org/wiki/League_(unit)> """  # noqa: E501
    LEAGUE = "league"
    """# <https://en.wikipedia.org/wiki/List_of_nautical_units_of_measurement> """  # noqa: E501
    NAUTICAL_LEAGUE = "nautical_league"
    """# <https://en.wikipedia.org/wiki/Yard> """  # noqa: E501
    YARD = "yard"

    def __str__(self) -> str:
        return str(self.value)
