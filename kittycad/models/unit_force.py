from enum import Enum


class UnitForce(str, Enum):
    """The valid types of force units."""  # noqa: E501

    """# Dynes <https://en.wikipedia.org/wiki/Dyne> """  # noqa: E501
    DYNES = "dynes"
    """# Kiloponds <https://en.wikipedia.org/wiki/Kilopond> """  # noqa: E501
    KILOPONDS = "kiloponds"
    """# Micronewtons <https://en.wikipedia.org/wiki/Newton_(unit)> """  # noqa: E501
    MICRONEWTONS = "micronewtons"
    """# Millinewtons <https://en.wikipedia.org/wiki/Newton_(unit)> """  # noqa: E501
    MILLINEWTONS = "millinewtons"
    """# Newtons <https://en.wikipedia.org/wiki/Newton_(unit)> """  # noqa: E501
    NEWTONS = "newtons"
    """# Poundals <https://en.wikipedia.org/wiki/Poundal> """  # noqa: E501
    POUNDALS = "poundals"
    """# Pounds <https://en.wikipedia.org/wiki/Pound_(force)> """  # noqa: E501
    POUNDS = "pounds"

    def __str__(self) -> str:
        return str(self.value)
