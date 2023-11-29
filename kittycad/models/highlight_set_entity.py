from typing import Optional
from uuid import UUID

from pydantic import BaseModel



class HighlightSetEntity(BaseModel):
    """The response from the `HighlightSetEntity` command."""

    entity_id: Optional[UUID] = None

    sequence: Optional[int] = None
