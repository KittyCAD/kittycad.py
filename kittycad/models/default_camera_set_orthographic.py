from pydantic import BaseModel, ConfigDict


class DefaultCameraSetOrthographic(BaseModel):
    """The response from the `DefaultCameraSetOrthographic` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
