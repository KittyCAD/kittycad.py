from enum import Enum


class CameraDragInteractionType(str, Enum):
    """The type of camera drag interaction."""  # noqa: E501

    """# Camera pan """  # noqa: E501
    PAN = "pan"
    """# Camera rotate (revolve/orbit) """  # noqa: E501
    ROTATE = "rotate"
    """# Camera zoom (increase or decrease distance to reference point center) """  # noqa: E501
    ZOOM = "zoom"

    def __str__(self) -> str:
        return str(self.value)
