from enum import Enum


class CurveTypeDebug(str, Enum):
    """What type of curve is being viewed?"""  # noqa: E501

    """# Line with a start and end."""  # noqa: E501

    LINE = "line"

    """# Arc with a start, end and center."""  # noqa: E501

    THREE_POINT_ARC = "three_point_arc"

    """# Circle with a center and radius."""  # noqa: E501

    CIRCLE = "circle"

    def __str__(self) -> str:
        return str(self.value)
