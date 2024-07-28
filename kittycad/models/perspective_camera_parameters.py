from typing import Optional

from pydantic import BaseModel, ConfigDict



class PerspectiveCameraParameters(BaseModel):
    """Defines a perspective view."""

    fov_y: Optional[float] = None

    z_far: Optional[float] = None

    z_near: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
