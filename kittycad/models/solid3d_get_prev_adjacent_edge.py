from typing import Optional

from pydantic import BaseModel



class Solid3dGetPrevAdjacentEdge(BaseModel):
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""

    edge: Optional[str] = None
