from pydantic import BaseModel, ConfigDict


class EntityMirrorAcrossEdge(BaseModel):
    """The response from the `EntityMirrorAcrossEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
