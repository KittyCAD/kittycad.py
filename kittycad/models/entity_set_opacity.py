from pydantic import BaseModel, ConfigDict


class EntitySetOpacity(BaseModel):
    """The response from the `EntitySetOpacity` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
