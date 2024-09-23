from pydantic import BaseModel, ConfigDict


class SetSceneUnits(BaseModel):
    """The response from the `SetSceneUnits` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
