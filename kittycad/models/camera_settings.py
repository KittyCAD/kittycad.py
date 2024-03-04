from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class CameraSettings(BaseModel):
    """Camera settings including position, center, fov etc"""

    center: Point3d

    fov_y: Optional[float] = None

    ortho: bool

    ortho_scale: Optional[float] = None

    pos: Point3d

    up: Point3d

    model_config = ConfigDict(protected_namespaces=())
