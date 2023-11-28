from enum import Enum


class AnnotationTextAlignmentX(str, Enum):
    """Horizontal Text alignment"""  # noqa: E501

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
