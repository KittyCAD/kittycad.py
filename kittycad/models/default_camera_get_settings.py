from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class Defaultcameragetsettings(BaseModel):
    """The response from the `DefaultCameraGetSettings` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
