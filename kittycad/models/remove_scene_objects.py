from pydantic import BaseModel, ConfigDict


class Removesceneobjects(BaseModel):
    """The response from the `RemoveSceneObjects` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
