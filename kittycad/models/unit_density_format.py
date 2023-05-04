from enum import Enum


class UnitDensityFormat(str, Enum):
    """The valid types of density unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Kilogram_per_cubic_metre> """  # noqa: E501
    KILOGRAMS_PER_CUBIC_METER = "kilograms_per_cubic_meter"
    """# <https://en.wikipedia.org/wiki/Specific_density> """  # noqa: E501
    GRAMS_PER_MILLILITER = "grams_per_milliliter"
    """# <https://en.wikipedia.org/wiki/Kilogram_per_cubic_metre> """  # noqa: E501
    KILOGRAMS_PER_LITER = "kilograms_per_liter"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    OUNCES_PER_CUBIC_FOOT = "ounces_per_cubic_foot"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    OUNCES_PER_CUBIC_INCH = "ounces_per_cubic_inch"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    OUNCES_PER_GALLON = "ounces_per_gallon"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    POUNDS_PER_CUBIC_FOOT = "pounds_per_cubic_foot"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    POUNDS_PER_CUBIC_INCH = "pounds_per_cubic_inch"
    """# <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    POUNDS_PER_GALLON = "pounds_per_gallon"
    """# <https://en.wikipedia.org/wiki/Slug_(unit)> and <https://en.wikipedia.org/wiki/Density#Unit> """  # noqa: E501
    SLUGS_PER_CUBIC_FOOT = "slugs_per_cubic_foot"

    def __str__(self) -> str:
        return str(self.value)
