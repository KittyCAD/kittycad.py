from enum import Enum


class UnitVolume(str, Enum):
    """The valid types of volume units."""  # noqa: E501

    """# Cubic centimeters (cc or cm³) <https://en.wikipedia.org/wiki/Cubic_centimeter> """  # noqa: E501
    CM3 = "cm3"
    """# Cubic feet (ft³) <https://en.wikipedia.org/wiki/Cubic_foot> """  # noqa: E501
    FT3 = "ft3"
    """# Cubic inches (cu in or in³) <https://en.wikipedia.org/wiki/Cubic_inch> """  # noqa: E501
    IN3 = "in3"
    """# Cubic meters (m³) <https://en.wikipedia.org/wiki/Cubic_meter> """  # noqa: E501
    M3 = "m3"
    """# Cubic yards (yd³) <https://en.wikipedia.org/wiki/Cubic_yard> """  # noqa: E501
    YD3 = "yd3"
    """# US Fluid Ounces (fl oz) <https://en.wikipedia.org/wiki/Fluid_ounce> """  # noqa: E501
    USFLOZ = "usfloz"
    """# US Gallons (gal US) <https://en.wikipedia.org/wiki/Gallon> """  # noqa: E501
    USGAL = "usgal"
    """# Liters (l) <https://en.wikipedia.org/wiki/Litre> """  # noqa: E501
    L = "l"
    """# Milliliters (ml) <https://en.wikipedia.org/wiki/Litre> """  # noqa: E501
    ML = "ml"

    def __str__(self) -> str:
        return str(self.value)
