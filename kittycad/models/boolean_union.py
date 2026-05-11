from typing import List, Optional

from .base import KittyCadBaseModel


class BooleanUnion(KittyCadBaseModel):
    """The response from the 'BooleanUnion'."""

    any_intersections: Optional[bool] = None

    extra_solid_ids: Optional[List[str]] = None
