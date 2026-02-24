from enum import Enum


class BlendType(str, Enum):
    """What kind of blend to do"""  # noqa: E501

    """# Use the tangent of the surfaces to calculate the blend."""  # noqa: E501

    TANGENT = "tangent"

    def __str__(self) -> str:
        return str(self.value)
