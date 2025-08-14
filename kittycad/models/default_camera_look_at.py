from pydantic import BaseModel, ConfigDict


class Defaultcameralookat(BaseModel):
    """The response from the `DefaultCameraLookAt` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
