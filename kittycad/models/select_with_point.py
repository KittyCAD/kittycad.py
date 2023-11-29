from typing import Optional
from uuid import UUID

from pydantic import BaseModel



class SelectWithPoint(BaseModel):
    """The response from the `SelectWithPoint` command."""

    entity_id: Optional[UUID] = None
