from pydantic import BaseModel, ConfigDict


class DefaultCameraSetView(BaseModel):
    """The response from the `DefaultCameraSetView` command."""

    model_config = ConfigDict(protected_namespaces=())
