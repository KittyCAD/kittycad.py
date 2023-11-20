from enum import Enum


class PathComponentConstraintType(str, Enum):
    """The path component constraint type"""  # noqa: E501

    UNCONSTRAINED = "unconstrained"
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
    EQUAL_LENGTH = "equal_length"
    PARALLEL = "parallel"
    ANGLE_BETWEEN = "angle_between"

    def __str__(self) -> str:
        return str(self.value)
