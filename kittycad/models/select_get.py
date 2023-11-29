from typing import List
from uuid import UUID

from pydantic import BaseModel


class SelectGet(BaseModel):
    """The response from the `SelectGet` command."""

    entity_ids: List[UUID]
