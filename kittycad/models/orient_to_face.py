from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class Orienttoface(BaseModel):
    """The response from the `OrientToFace` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
