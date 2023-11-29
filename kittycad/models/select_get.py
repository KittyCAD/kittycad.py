from typing import List

from pydantic import BaseModel



class SelectGet(BaseModel):
    """The response from the `SelectGet` command."""

    entity_ids: List[str]
