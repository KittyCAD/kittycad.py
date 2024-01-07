
from pydantic import BaseModel, ConfigDict



class EntityGetChildUuid(BaseModel):
    """The response from the `EntityGetChildUuid` command."""

    entity_id: str

    model_config = ConfigDict(protected_namespaces=())
