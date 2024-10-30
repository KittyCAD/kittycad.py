from enum import Enum


class CameraMovement(str, Enum):
    """A type of camera movement applied after certain camera operations"""  # noqa: E501

    """# Adjusts the camera position during the camera operation """  # noqa: E501
    VANTAGE = "vantage"
    """# Keeps the camera position in place """  # noqa: E501
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
