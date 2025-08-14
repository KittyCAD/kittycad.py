from pydantic import BaseModel, ConfigDict


class Defaultcamerasetperspective(BaseModel):
    """The response from the `DefaultCameraSetPerspective` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
