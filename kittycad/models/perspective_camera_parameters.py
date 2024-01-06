
from pydantic import BaseModel



class PerspectiveCameraParameters(BaseModel):
    """Defines a perspective view."""

    fov_y: float

    z_far: float

    z_near: float
