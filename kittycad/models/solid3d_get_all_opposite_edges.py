from typing import List
from uuid import UUID

from pydantic import BaseModel



class Solid3dGetAllOppositeEdges(BaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    edges: List[UUID]
