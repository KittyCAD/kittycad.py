from enum import Enum


class UnitFrequency(str, Enum):
    """The valid types of frequency units."""  # noqa: E501

    """# Gigahertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    GIGAHERTZ = "gigahertz"
    """# Hertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    HERTZ = "hertz"
    """# Kilohertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    KILOHERTZ = "kilohertz"
    """# Megahertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    MEGAHERTZ = "megahertz"
    """# Microhertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    MICROHERTZ = "microhertz"
    """# Millihertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    MILLIHERTZ = "millihertz"
    """# Nanohertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    NANOHERTZ = "nanohertz"
    """# Terahertz <https://en.wikipedia.org/wiki/Hertz> """  # noqa: E501
    TERAHERTZ = "terahertz"

    def __str__(self) -> str:
        return str(self.value)
