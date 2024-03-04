from enum import Enum


class UnitDensity(str, Enum):
    """The valid types for density units."""  # noqa: E501

    """# Pounds per cubic feet. """  # noqa: E501
    LB_FT3 = "lb:ft3"
    """# Kilograms per cubic meter. """  # noqa: E501
    KG_M3 = "kg:m3"

    def __str__(self) -> str:
        return str(self.value)
