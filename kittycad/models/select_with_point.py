from typing import Optional

from pydantic import BaseModel



class SelectWithPoint(BaseModel):
    """The response from the `SelectWithPoint` command."""

    entity_id: Optional[str] = None
