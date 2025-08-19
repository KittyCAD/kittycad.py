from enum import Enum


class RelativeTo(str, Enum):
    """What is the given geometry relative to?"""  # noqa: E501

    """# Local/relative to a position centered within the plane being sketched on"""  # noqa: E501

    SKETCH_PLANE = "sketch_plane"

    """# Local/relative to the trajectory curve"""  # noqa: E501

    TRAJECTORY_CURVE = "trajectory_curve"

    def __str__(self) -> str:
        return str(self.value)
