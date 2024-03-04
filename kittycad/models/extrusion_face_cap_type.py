from enum import Enum


class ExtrusionFaceCapType(str, Enum):
    """Possible types of faces which can be extruded from a 3D solid."""  # noqa: E501

    """# Uncapped. """  # noqa: E501
    NONE = "none"
    """# Capped on top. """  # noqa: E501
    TOP = "top"
    """# Capped below. """  # noqa: E501
    BOTTOM = "bottom"

    def __str__(self) -> str:
        return str(self.value)
