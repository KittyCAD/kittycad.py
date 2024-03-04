from enum import Enum


class SceneToolType(str, Enum):
    """The type of scene's active tool"""  # noqa: E501

    CAMERA_REVOLVE = "camera_revolve"
    SELECT = "select"
    MOVE = "move"
    SKETCH_LINE = "sketch_line"
    SKETCH_TANGENTIAL_ARC = "sketch_tangential_arc"
    SKETCH_CURVE = "sketch_curve"
    SKETCH_CURVE_MOD = "sketch_curve_mod"

    def __str__(self) -> str:
        return str(self.value)
