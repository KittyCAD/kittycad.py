from pydantic import BaseModel, ConfigDict


class EntityMirror(BaseModel):
    """The response from the `EntityMirror` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
