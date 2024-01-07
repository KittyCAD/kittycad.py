
from pydantic import BaseModel, ConfigDict



class PerspectiveCameraParameters(BaseModel):
    """Defines a perspective view."""

    fov_y: float

    z_far: float

    z_near: float

    model_config = ConfigDict(protected_namespaces=())
