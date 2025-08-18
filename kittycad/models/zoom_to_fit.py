from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class ZoomToFit(KittyCadBaseModel):
    """The response from the `ZoomToFit` command."""

    settings: CameraSettings
