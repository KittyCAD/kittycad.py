from typing import List

from pydantic import BaseModel



class Solid3dGetAllOppositeEdges(BaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    edges: List[str]
