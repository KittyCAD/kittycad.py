from typing import List
from uuid import UUID

from pydantic import BaseModel



class EntityGetAllChildUuids(BaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    entity_ids: List[UUID]
