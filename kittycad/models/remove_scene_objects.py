from pydantic import BaseModel, ConfigDict


class RemoveSceneObjects(BaseModel):
    """The response from the `RemoveSceneObjects` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
