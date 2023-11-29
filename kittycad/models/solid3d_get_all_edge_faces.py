from typing import List

from pydantic import BaseModel



class Solid3dGetAllEdgeFaces(BaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    faces: List[str]
