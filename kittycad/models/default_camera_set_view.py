from pydantic import BaseModel, ConfigDict


class Defaultcamerasetview(BaseModel):
    """The response from the `DefaultCameraSetView` command."""

    model_config = ConfigDict(protected_namespaces=())
