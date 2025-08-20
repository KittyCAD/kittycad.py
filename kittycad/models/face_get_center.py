from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class FaceGetCenter(KittyCadBaseModel):
    """The 3D center of mass on the surface"""

    pos: Point3d
