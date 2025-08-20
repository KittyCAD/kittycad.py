from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class CameraDragEnd(KittyCadBaseModel):
    """The response from the `CameraDragEnd` command."""

    settings: CameraSettings
