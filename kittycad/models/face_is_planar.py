from typing import Optional

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class FaceIsPlanar(KittyCadBaseModel):
    """Surface-local planar axes (if available)"""

    origin: Optional[Point3d] = None

    x_axis: Optional[Point3d] = None

    y_axis: Optional[Point3d] = None

    z_axis: Optional[Point3d] = None
