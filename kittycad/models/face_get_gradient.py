from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class FaceGetGradient(KittyCadBaseModel):
    """The gradient (dFdu, dFdv) + normal vector on a brep face"""

    df_du: Point3d

    df_dv: Point3d

    normal: Point3d
