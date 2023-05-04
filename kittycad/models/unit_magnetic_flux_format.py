from enum import Enum


class UnitMagneticFluxFormat(str, Enum):
    """The valid types of magnetic flux unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Weber_(unit)> """  # noqa: E501
    WEBER = "weber"
    """# <https://en.wikipedia.org/wiki/Maxwell_(unit)> """  # noqa: E501
    MAXWELL = "maxwell"

    def __str__(self) -> str:
        return str(self.value)
