from enum import Enum


class PathCommand(str, Enum):
    """The path component command type (within a Path)"""  # noqa: E501

    MOVE_TO = "move_to"
    LINE_TO = "line_to"
    BEZ_CURVE_TO = "bez_curve_to"
    NURBS_CURVE_TO = "nurbs_curve_to"
    ADD_ARC = "add_arc"

    def __str__(self) -> str:
        return str(self.value)
