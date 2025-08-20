from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class DefaultCameraZoom(KittyCadBaseModel):
    """The response from the `DefaultCameraZoom` command."""

    settings: CameraSettings
