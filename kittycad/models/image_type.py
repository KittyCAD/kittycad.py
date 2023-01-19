from enum import Enum


class ImageType(str, Enum):
    PNG = 'png'
    JPG = 'jpg'

    def __str__(self) -> str:
        return str(self.value)
