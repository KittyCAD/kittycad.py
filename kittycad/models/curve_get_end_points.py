from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class CurveGetEndPoints(KittyCadBaseModel):
    """Endpoints of a curve"""

    end: Point3d

    start: Point3d
