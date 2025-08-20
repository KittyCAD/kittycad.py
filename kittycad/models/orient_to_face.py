from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class OrientToFace(KittyCadBaseModel):
    """The response from the `OrientToFace` command."""

    settings: CameraSettings
