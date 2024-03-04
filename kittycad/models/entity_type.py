from enum import Enum


class EntityType(str, Enum):
    """The type of entity"""  # noqa: E501

    ENTITY = "entity"
    OBJECT = "object"
    PATH = "path"
    CURVE = "curve"
    SOLID2D = "solid2d"
    SOLID3D = "solid3d"
    EDGE = "edge"
    FACE = "face"
    PLANE = "plane"
    VERTEX = "vertex"

    def __str__(self) -> str:
        return str(self.value)
