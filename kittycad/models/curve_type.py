from enum import Enum


class CurveType(str, Enum):
    """The type of Curve (embedded within path)"""  # noqa: E501

    LINE = "line"
    ARC = "arc"
    NURBS = "nurbs"

    def __str__(self) -> str:
        return str(self.value)
