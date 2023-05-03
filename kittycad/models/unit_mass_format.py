from enum import Enum


class UnitMassFormat(str, Enum):
    """The valid types of mass unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Gram> """  # noqa: E501
    GRAM = "gram"
    """# <https://en.wikipedia.org/wiki/Kilogram> """  # noqa: E501
    KILOGRAM = "kilogram"
    """# <https://en.wikipedia.org/wiki/Tonne> """  # noqa: E501
    METRIC_TON = "metric_ton"
    """# <https://en.wikipedia.org/wiki/Pound_(mass)> """  # noqa: E501
    POUND = "pound"
    """# <https://en.wikipedia.org/wiki/Long_ton> """  # noqa: E501
    LONG_TON = "long_ton"
    """# <https://en.wikipedia.org/wiki/Short_ton> """  # noqa: E501
    SHORT_TON = "short_ton"
    """# <https://en.wikipedia.org/wiki/Stone_(unit)> """  # noqa: E501
    STONE = "stone"
    """# <https://en.wikipedia.org/wiki/Ounce> """  # noqa: E501
    OUNCE = "ounce"
    """# <https://en.wikipedia.org/wiki/Carat_(mass)> """  # noqa: E501
    CARAT = "carat"
    """# <https://en.wikipedia.org/wiki/Slug_(unit)> """  # noqa: E501
    SLUG = "slug"

    def __str__(self) -> str:
        return str(self.value)
