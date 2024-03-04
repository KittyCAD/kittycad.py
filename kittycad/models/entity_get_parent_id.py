
from pydantic import BaseModel, ConfigDict



class EntityGetParentId(BaseModel):
    """The response from the `EntityGetParentId` command."""

    entity_id: str

    model_config = ConfigDict(protected_namespaces=())
