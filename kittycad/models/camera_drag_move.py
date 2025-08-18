from ..models.camera_settings import CameraSettings
from .base import KittyCadBaseModel


class CameraDragMove(KittyCadBaseModel):
    """The response from the `CameraDragMove` command. Note this is an \"unreliable\" channel message, so this data may need more data like a \"sequence\" """

    settings: CameraSettings
