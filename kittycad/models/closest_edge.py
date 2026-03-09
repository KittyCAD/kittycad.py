from typing import Optional

from .base import KittyCadBaseModel


class ClosestEdge(KittyCadBaseModel):
    """The response from the 'ClosestEdge'."""

    edge_id: Optional[str] = None
