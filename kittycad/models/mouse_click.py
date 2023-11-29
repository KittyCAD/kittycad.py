from typing import List

from pydantic import BaseModel



class MouseClick(BaseModel):
    """The response from the `MouseClick` command."""

    entities_modified: List[str]

    entities_selected: List[str]
