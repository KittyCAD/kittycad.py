from pydantic import BaseModel, ConfigDict

from ..models.camera_view_state import CameraViewState


class Defaultcameragetview(BaseModel):
    """The response from the `DefaultCameraGetView` command."""

    view: CameraViewState

    model_config = ConfigDict(protected_namespaces=())
