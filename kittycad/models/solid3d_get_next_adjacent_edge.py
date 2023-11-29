from typing import Optional

from pydantic import BaseModel



class Solid3dGetNextAdjacentEdge(BaseModel):
    """The response from the `Solid3dGetNextAdjacentEdge` command."""

    edge: Optional[str] = None
