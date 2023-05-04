from enum import Enum


class UnitRadiationFormat(str, Enum):
    """The valid types of radiation unit formats. These describe the radiation energy absorbed by a mass or material and/or how it affects the relative damage to the human body."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Gray_(unit)> """  # noqa: E501
    GRAY = "gray"
    """# <https://en.wikipedia.org/wiki/Sievert> """  # noqa: E501
    SIEVERT = "sievert"
    """# <https://en.wikipedia.org/wiki/Rad_(unit)> """  # noqa: E501
    RAD = "rad"

    def __str__(self) -> str:
        return str(self.value)
