from pydantic import BaseModel, ConfigDict


class DefaultCameraPerspectiveSettings(BaseModel):
    """The response from the `DefaultCameraPerspectiveSettings` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
