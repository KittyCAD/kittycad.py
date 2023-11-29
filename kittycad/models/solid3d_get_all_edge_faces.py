from typing import List
from uuid import UUID

from pydantic import BaseModel


class Solid3dGetAllEdgeFaces(BaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    faces: List[UUID]
