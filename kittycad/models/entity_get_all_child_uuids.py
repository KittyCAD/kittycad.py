from typing import List

from pydantic import BaseModel



class EntityGetAllChildUuids(BaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    entity_ids: List[str]
