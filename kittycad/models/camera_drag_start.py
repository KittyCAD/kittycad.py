from pydantic import BaseModel, ConfigDict


class CameraDragStart(BaseModel):
    """The response from the `CameraDragStart` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
