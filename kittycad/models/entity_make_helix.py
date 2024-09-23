from pydantic import BaseModel, ConfigDict


class EntityMakeHelix(BaseModel):
    """The response from the `EntityMakeHelix` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
