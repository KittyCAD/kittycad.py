from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class Defaultcamerazoom(BaseModel):
    """The response from the `DefaultCameraZoom` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
