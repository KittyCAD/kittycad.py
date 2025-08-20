from ..models.camera_view_state import CameraViewState
from .base import KittyCadBaseModel


class DefaultCameraGetView(KittyCadBaseModel):
    """The response from the `DefaultCameraGetView` command."""

    view: CameraViewState
