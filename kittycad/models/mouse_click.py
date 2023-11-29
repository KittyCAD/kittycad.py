from typing import List
from uuid import UUID

from pydantic import BaseModel


class MouseClick(BaseModel):
    """The response from the `MouseClick` command."""

    entities_modified: List[UUID]

    entities_selected: List[UUID]
