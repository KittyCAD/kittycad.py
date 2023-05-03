from enum import Enum


class UnitForceFormat(str, Enum):
    """The valid types of force unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Newton_(unit)> """  # noqa: E501
    NEWTON = "newton"
    """# <https://en.wikipedia.org/wiki/Pound_(force)> """  # noqa: E501
    POUND = "pound"
    """# <https://en.wikipedia.org/wiki/Dyne> """  # noqa: E501
    DYNE = "dyne"
    """# <https://en.wikipedia.org/wiki/Kilogram-force> """  # noqa: E501
    KILOPOND = "kilopond"
    """# <https://en.wikipedia.org/wiki/Poundal> """  # noqa: E501
    POUNDAL = "poundal"

    def __str__(self) -> str:
        return str(self.value)
