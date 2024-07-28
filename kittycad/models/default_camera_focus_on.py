
from pydantic import BaseModel, ConfigDict



class DefaultCameraFocusOn(BaseModel):
    """The response from the `DefaultCameraFocusOn` command."""

    model_config = ConfigDict(protected_namespaces=())
