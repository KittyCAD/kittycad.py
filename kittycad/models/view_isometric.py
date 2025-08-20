from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class ViewIsometric(KittyCadBaseModel):
    """The response from the `ViewIsometric` command."""

    settings: CameraSettings
