from typing import Optional

from ..models.point3d import Point3d
from ..models.point4d import Point4d
from .base import KittyCadBaseModel


class CameraSettings(KittyCadBaseModel):
    """Camera settings including position, center, fov etc"""

    center: Point3d

    fov_y: Optional[float] = None

    orientation: Point4d

    ortho: bool

    ortho_scale: Optional[float] = None

    pos: Point3d

    up: Point3d
