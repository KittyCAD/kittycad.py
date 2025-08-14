from pydantic import BaseModel, ConfigDict


class Cameradragstart(BaseModel):
    """The response from the `CameraDragStart` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
