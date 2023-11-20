from enum import Enum


class ImageFormat(str, Enum):
    """Enum containing the variety of image formats snapshots may be exported to."""  # noqa: E501

    """# .png format """  # noqa: E501
    PNG = "png"
    """# .jpeg format """  # noqa: E501
    JPEG = "jpeg"

    def __str__(self) -> str:
        return str(self.value)
