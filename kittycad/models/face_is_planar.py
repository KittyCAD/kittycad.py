from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class FaceIsPlanar(BaseModel):
    """Surface-local planar axes (if available)"""

    origin: Optional[Point3d] = None

    x_axis: Optional[Point3d] = None

    y_axis: Optional[Point3d] = None

    z_axis: Optional[Point3d] = None

    model_config = ConfigDict(protected_namespaces=())
