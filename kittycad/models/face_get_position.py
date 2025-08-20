from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class FaceGetPosition(KittyCadBaseModel):
    """The 3D position on the surface that was evaluated"""

    pos: Point3d
