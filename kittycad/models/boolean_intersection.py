from typing import List, Optional

from .base import KittyCadBaseModel


class BooleanIntersection(KittyCadBaseModel):
    """The response from the 'BooleanIntersection'."""

    extra_solid_ids: Optional[List[str]] = None
