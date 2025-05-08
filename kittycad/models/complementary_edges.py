from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ComplementaryEdges(BaseModel):
    """Struct to contain the edge information of a wall of an extrude/rotate/loft/sweep."""

    adjacent_ids: List[str]

    opposite_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
