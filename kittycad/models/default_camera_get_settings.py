from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class DefaultCameraGetSettings(KittyCadBaseModel):
    """The response from the `DefaultCameraGetSettings` command."""

    settings: CameraSettings
