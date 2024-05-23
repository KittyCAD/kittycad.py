
from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class ZoomToFit(BaseModel):
    """The response from the `ZoomToFit` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
