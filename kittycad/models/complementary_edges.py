from typing import List, Optional

from .base import KittyCadBaseModel


class ComplementaryEdges(KittyCadBaseModel):
    """Struct to contain the edge information of a wall of an extrude/rotate/loft/sweep."""

    adjacent_ids: List[str]

    opposite_id: Optional[str] = None
