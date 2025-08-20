from typing import Optional

from .base import KittyCadBaseModel


class Solid3dGetNextAdjacentEdge(KittyCadBaseModel):
    """The response from the `Solid3dGetNextAdjacentEdge` command."""

    edge: Optional[str] = None
