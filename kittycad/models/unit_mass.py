from enum import Enum


class UnitMass(str, Enum):
    """The valid types of mass units."""  # noqa: E501

    """# Grams <https://en.wikipedia.org/wiki/Gram> """  # noqa: E501
    G = "g"
    """# Kilograms <https://en.wikipedia.org/wiki/Kilogram> """  # noqa: E501
    KG = "kg"
    """# Pounds <https://en.wikipedia.org/wiki/Pound_(mass)> """  # noqa: E501
    LB = "lb"

    def __str__(self) -> str:
        return str(self.value)
