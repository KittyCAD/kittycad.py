from pydantic import BaseModel, ConfigDict


class EntityMakeHelixFromEdge(BaseModel):
    """The response from the `EntityMakeHelixFromEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
