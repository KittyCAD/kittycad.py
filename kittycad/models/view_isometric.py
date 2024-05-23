
from pydantic import BaseModel, ConfigDict

from ..models.camera_settings import CameraSettings


class ViewIsometric(BaseModel):
    """The response from the `ViewIsometric` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
