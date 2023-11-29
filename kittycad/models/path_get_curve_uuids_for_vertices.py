from typing import List
from uuid import UUID

from pydantic import BaseModel



class PathGetCurveUuidsForVertices(BaseModel):
    """The response from the `PathGetCurveUuidsForVertices` command."""

    curve_ids: List[UUID]
