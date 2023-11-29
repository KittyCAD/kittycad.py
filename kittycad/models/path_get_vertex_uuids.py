from typing import List
from uuid import UUID

from pydantic import BaseModel



class PathGetVertexUuids(BaseModel):
    """The response from the `PathGetVertexUuids` command."""

    vertex_ids: List[UUID]
