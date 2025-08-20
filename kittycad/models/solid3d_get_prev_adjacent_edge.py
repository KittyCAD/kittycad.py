from typing import Optional

from .base import KittyCadBaseModel


class Solid3dGetPrevAdjacentEdge(KittyCadBaseModel):
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""

    edge: Optional[str] = None
