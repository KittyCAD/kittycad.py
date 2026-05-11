from typing import List, Optional

from .base import KittyCadBaseModel


class BooleanSubtract(KittyCadBaseModel):
    """The response from the 'BooleanSubtract'."""

    any_intersections: Optional[bool] = None

    extra_solid_ids: Optional[List[str]] = None
