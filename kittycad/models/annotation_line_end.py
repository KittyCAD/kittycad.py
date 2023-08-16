from enum import Enum


class AnnotationLineEnd(str, Enum):
    """Annotation line end type"""  # noqa: E501

    NONE = "none"
    ARROW = "arrow"

    def __str__(self) -> str:
        return str(self.value)
