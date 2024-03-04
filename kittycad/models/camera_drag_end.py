
from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class CameraDragEnd(BaseModel):
    """The response from the `CameraDragEnd` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
