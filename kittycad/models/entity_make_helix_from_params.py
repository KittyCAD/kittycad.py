from pydantic import BaseModel, ConfigDict


class EntityMakeHelixFromParams(BaseModel):
    """The response from the `EntityMakeHelixFromParams` endpoint."""

    helix_id: str

    model_config = ConfigDict(protected_namespaces=())
