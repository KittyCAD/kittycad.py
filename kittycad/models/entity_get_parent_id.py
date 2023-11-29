
from pydantic import BaseModel



class EntityGetParentId(BaseModel):
    """The response from the `EntityGetParentId` command."""

    entity_id: str
