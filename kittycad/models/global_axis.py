from enum import Enum


class GlobalAxis(str, Enum):
    """An enum that contains the three global axes."""  # noqa: E501

    """# The X axis """  # noqa: E501
    X = "x"
    """# The Y axis """  # noqa: E501
    Y = "y"
    """# The Z axis """  # noqa: E501
    Z = "z"

    def __str__(self) -> str:
        return str(self.value)
