from pydantic import BaseModel, ConfigDict


class DefaultCameraSetPerspective(BaseModel):
    """The response from the `DefaultCameraSetPerspective` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
