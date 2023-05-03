from enum import Enum


class UnitVolumeFormat(str, Enum):
    """The valid types of volume unit formats."""  # noqa: E501

    """# Unit Meter <https://en.wikipedia.org/wiki/Cubic_metre> """  # noqa: E501
    CUBIC_METER = "cubic_meter"
    """# Centimeter <https://en.wikipedia.org/wiki/Centimetre> """  # noqa: E501
    CUBIC_CENTIMETER = "cubic_centimeter"
    """# Millimeter <https://en.wikipedia.org/wiki/Cubic_metre> """  # noqa: E501
    CUBIC_MILLIMETER = "cubic_millimeter"
    """# Kilometer <https://en.wikipedia.org/wiki/Cubic_metre> """  # noqa: E501
    CUBIC_KILOMETER = "cubic_kilometer"
    """# Unit Liter <https://en.wikipedia.org/wiki/Litre> """  # noqa: E501
    LITER = "liter"
    """# Cubic Inch <https://en.wikipedia.org/wiki/Cubic_inch> """  # noqa: E501
    CUBIC_INCH = "cubic_inch"
    """# Foot <https://en.wikipedia.org/wiki/Cubic_foot> """  # noqa: E501
    CUBIC_FOOT = "cubic_foot"
    """# Yard <https://en.wikipedia.org/wiki/Cubic_foot> """  # noqa: E501
    CUBIC_YARD = "cubic_yard"
    """# Mile <https://en.wikipedia.org/wiki/Cubic_foot> """  # noqa: E501
    CUBIC_MILE = "cubic_mile"
    """# Gallon <https://en.wikipedia.org/wiki/Gallon> """  # noqa: E501
    GALLON = "gallon"
    """# Quart <https://en.wikipedia.org/wiki/Quart> """  # noqa: E501
    QUART = "quart"
    """# Pint <https://en.wikipedia.org/wiki/Pint> """  # noqa: E501
    PINT = "pint"
    """# Cup <https://en.wikipedia.org/wiki/Cup_(unit)> """  # noqa: E501
    CUP = "cup"
    """# Fluid Ounce <https://en.wikipedia.org/wiki/Fluid_ounce> """  # noqa: E501
    FLUID_OUNCE = "fluid_ounce"
    """# Barrel <https://en.wikipedia.org/wiki/Barrel_(unit)> """  # noqa: E501
    BARREL = "barrel"
    """# Bushel <https://en.wikipedia.org/wiki/Bushel> """  # noqa: E501
    BUSHEL = "bushel"
    """# Cord <https://en.wikipedia.org/wiki/Cord_(unit)> """  # noqa: E501
    CORD = "cord"
    """# Cubic Fathom <https://en.wikipedia.org/wiki/Cubic_fathom> """  # noqa: E501
    CUBIC_FATHOM = "cubic_fathom"
    """# Tablespoon <https://en.wikipedia.org/wiki/Tablespoon> """  # noqa: E501
    TABLESPOON = "tablespoon"
    """# Teaspoon <https://en.wikipedia.org/wiki/Teaspoon> """  # noqa: E501
    TEASPOON = "teaspoon"
    """# Pinch <https://en.wikipedia.org/wiki/Pinch_(unit)> """  # noqa: E501
    PINCH = "pinch"
    """# Dash <https://en.wikipedia.org/wiki/Cooking_weights_and_measures> """  # noqa: E501
    DASH = "dash"
    """# Drop <https://en.wikipedia.org/wiki/Cooking_weights_and_measures> """  # noqa: E501
    DROP = "drop"
    """# Fifth <https://en.wikipedia.org/wiki/Fifth_(unit)> """  # noqa: E501
    FIFTH = "fifth"
    """# Dram <https://en.wikipedia.org/wiki/Dram_(unit)> """  # noqa: E501
    DRAM = "dram"
    """# Gill <https://en.wikipedia.org/wiki/Gill_(unit)> """  # noqa: E501
    GILL = "gill"
    """# Peck <https://en.wikipedia.org/wiki/Imperial_units> """  # noqa: E501
    PECK = "peck"
    """# Stack <https://en.wikipedia.org/wiki/Stack_(unit)> """  # noqa: E501
    SACK = "sack"
    """# Shot <https://en.wikipedia.org/wiki/Shot_glass> """  # noqa: E501
    SHOT = "shot"
    """# Strike <https://en.wikipedia.org/wiki/Strike_(unit)> """  # noqa: E501
    STRIKE = "strike"

    def __str__(self) -> str:
        return str(self.value)
