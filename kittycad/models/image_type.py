from enum import Enum


class ImageType(str, Enum):
    """An enumeration."""  # noqa: E501

    PNG = "png"
    JPG = "jpg"

    def __str__(self) -> str:
        return str(self.value)
