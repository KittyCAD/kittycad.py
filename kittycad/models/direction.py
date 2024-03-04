from enum import Enum


class Direction(str, Enum):
    """Specifies the sign of a co-ordinate axis."""  # noqa: E501

    """# Increasing numbers. """  # noqa: E501
    POSITIVE = "positive"
    """# Decreasing numbers. """  # noqa: E501
    NEGATIVE = "negative"

    def __str__(self) -> str:
        return str(self.value)
