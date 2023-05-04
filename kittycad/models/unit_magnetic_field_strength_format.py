from enum import Enum


class UnitMagneticFieldStrengthFormat(str, Enum):
    """The valid types of magnetic field strength unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Tesla_(unit)> """  # noqa: E501
    TESLA = "tesla"
    """# <https://en.wikipedia.org/wiki/Gauss_(unit)> """  # noqa: E501
    GAUSS = "gauss"

    def __str__(self) -> str:
        return str(self.value)
