from typing import List

from .base import KittyCadBaseModel


class Solid3dGetAllEdgeFaces(KittyCadBaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    faces: List[str]
