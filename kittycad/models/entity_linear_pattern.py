from typing import List

from pydantic import BaseModel



class EntityLinearPattern(BaseModel):
    """The response from the `EntityLinearPattern` command."""

    entity_ids: List[str]
