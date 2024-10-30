from pydantic import BaseModel, ConfigDict


class DefaultCameraCenterToScene(BaseModel):
    """The response from the `DefaultCameraCenterToScene` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
