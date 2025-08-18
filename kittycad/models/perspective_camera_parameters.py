from typing import Optional

from .base import KittyCadBaseModel


class PerspectiveCameraParameters(KittyCadBaseModel):
    """Defines a perspective view."""

    fov_y: Optional[float] = None

    z_far: Optional[float] = None

    z_near: Optional[float] = None
