from uuid import UUID

from pydantic import BaseModel



class EntityGetChildUuid(BaseModel):
    """The response from the `EntityGetChildUuid` command."""

    entity_id: UUID
