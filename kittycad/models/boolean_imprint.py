from typing import List, Optional

from .base import KittyCadBaseModel


class BooleanImprint(KittyCadBaseModel):
    """The response from the 'BooleanImprint'."""

    any_intersections: Optional[bool] = None

    extra_solid_ids: Optional[List[str]] = None
