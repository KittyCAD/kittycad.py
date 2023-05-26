from enum import Enum


class UnitMass(str, Enum):
    """The valid types of mass units."""  # noqa: E501

    """# Carats <https://en.wikipedia.org/wiki/Carat_(mass)> """  # noqa: E501
    CARATS = "carats"
    """# Grains <https://en.wikipedia.org/wiki/Grain_(unit)> """  # noqa: E501
    GRAINS = "grains"
    """# Grams <https://en.wikipedia.org/wiki/Gram> """  # noqa: E501
    GRAMS = "grams"
    """# Kilograms <https://en.wikipedia.org/wiki/Kilogram> """  # noqa: E501
    KILOGRAMS = "kilograms"
    """# Long tons <https://en.wikipedia.org/wiki/Long_ton> """  # noqa: E501
    LONG_TONS = "long_tons"
    """# Metric tons <https://en.wikipedia.org/wiki/Tonne> """  # noqa: E501
    METRIC_TONS = "metric_tons"
    """# Micrograms <https://en.wikipedia.org/wiki/Microgram> """  # noqa: E501
    MICROGRAMS = "micrograms"
    """# Milligrams <https://en.wikipedia.org/wiki/Milligram> """  # noqa: E501
    MILLIGRAMS = "milligrams"
    """# Ounces <https://en.wikipedia.org/wiki/Ounce> """  # noqa: E501
    OUNCES = "ounces"
    """# Pennyweights <https://en.wikipedia.org/wiki/Pennyweight> """  # noqa: E501
    PENNYWEIGHTS = "pennyweights"
    """# Pounds <https://en.wikipedia.org/wiki/Pound_(mass)> """  # noqa: E501
    POUNDS = "pounds"
    """# Short tons <https://en.wikipedia.org/wiki/Short_ton> """  # noqa: E501
    SHORT_TONS = "short_tons"
    """# Stones <https://en.wikipedia.org/wiki/Stone_(unit)> """  # noqa: E501
    STONES = "stones"
    """# Troy ounces <https://en.wikipedia.org/wiki/Troy_ounce> """  # noqa: E501
    TROY_OUNCES = "troy_ounces"
    """# Troy pounds <https://en.wikipedia.org/wiki/Troy_pound> """  # noqa: E501
    TROY_POUNDS = "troy_pounds"

    def __str__(self) -> str:
        return str(self.value)
