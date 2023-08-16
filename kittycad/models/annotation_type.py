from enum import Enum


class AnnotationType(str, Enum):
    """The type of annotation"""  # noqa: E501

    """# 2D annotation type (screen or planar space) """  # noqa: E501
    T2D = "t2d"
    """# 3D annotation type """  # noqa: E501
    T3D = "t3d"

    def __str__(self) -> str:
        return str(self.value)
