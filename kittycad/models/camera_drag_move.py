
from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class CameraDragMove(BaseModel):
    """The response from the `CameraDragMove` command. Note this is an \"unreliable\" channel message, so this data may need more data like a \"sequence\" """

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
