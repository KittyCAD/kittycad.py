from enum import Enum


class PathComponentConstraintBound(str, Enum):
    """The path component constraint bounds type"""  # noqa: E501

    UNCONSTRAINED = "unconstrained"
    PARTIALLY_CONSTRAINED = "partially_constrained"
    FULLY_CONSTRAINED = "fully_constrained"

    def __str__(self) -> str:
        return str(self.value)
