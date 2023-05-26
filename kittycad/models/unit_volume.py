from enum import Enum


class UnitVolume(str, Enum):
    """The valid types of volume units."""  # noqa: E501

    """# Cubic centimeters (cc or cm³) <https://en.wikipedia.org/wiki/Cubic_centimetre> """  # noqa: E501
    CUBIC_CENTIMETRES = "cubic_centimetres"
    """# Cubic feet (ft³) <https://en.wikipedia.org/wiki/Cubic_foot> """  # noqa: E501
    CUBIC_FEET = "cubic_feet"
    """# Cubic inches (cu in or in³) <https://en.wikipedia.org/wiki/Cubic_inch> """  # noqa: E501
    CUBIC_INCHES = "cubic_inches"
    """# Cubic metres (m³) <https://en.wikipedia.org/wiki/Cubic_metre> """  # noqa: E501
    CUBIC_METRES = "cubic_metres"
    """# Cubic yards (yd³) <https://en.wikipedia.org/wiki/Cubic_yard> """  # noqa: E501
    CUBIC_YARDS = "cubic_yards"
    """# Cups <https://en.wikipedia.org/wiki/Cup_(unit)> """  # noqa: E501
    CUPS = "cups"
    """# Drams <https://en.wikipedia.org/wiki/Fluid_dram> """  # noqa: E501
    DRAMS = "drams"
    """# Drops <https://en.wikipedia.org/wiki/Minim_(unit)> """  # noqa: E501
    DROPS = "drops"
    """# US Fluid Ounces (fl oz) <https://en.wikipedia.org/wiki/Fluid_ounce> """  # noqa: E501
    FLUID_OUNCES = "fluid_ounces"
    """# UK Fluid Ounces (fl oz) <https://en.wikipedia.org/wiki/Fluid_ounce> """  # noqa: E501
    FLUID_OUNCES_UK = "fluid_ounces_uk"
    """# US Gallons (gal US) <https://en.wikipedia.org/wiki/Gallon> """  # noqa: E501
    GALLONS = "gallons"
    """# UK/Imperial Gallons (gal) <https://en.wikipedia.org/wiki/Gallon> """  # noqa: E501
    GALLONS_UK = "gallons_uk"
    """# Liters (l) <https://en.wikipedia.org/wiki/Litre> """  # noqa: E501
    LITRES = "litres"
    """# Milliliters (ml) <https://en.wikipedia.org/wiki/Litre> """  # noqa: E501
    MILLILITRES = "millilitres"
    """# Pints <https://en.wikipedia.org/wiki/Pint> """  # noqa: E501
    PINTS = "pints"
    """# Pints in the United Kingdom (UK) <https://en.wikipedia.org/wiki/Pint> """  # noqa: E501
    PINTS_UK = "pints_uk"
    """# Quarts <https://en.wikipedia.org/wiki/Quart> """  # noqa: E501
    QUARTS = "quarts"
    """# Tablespoons (tbsp) <https://en.wikipedia.org/wiki/Tablespoon> """  # noqa: E501
    TABLESPOONS = "tablespoons"
    """# Teaspoons (tsp) <https://en.wikipedia.org/wiki/Teaspoon> """  # noqa: E501
    TEASPOONS = "teaspoons"

    def __str__(self) -> str:
        return str(self.value)
