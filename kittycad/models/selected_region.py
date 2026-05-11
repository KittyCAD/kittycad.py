from typing import Optional

from .base import KittyCadBaseModel


class SelectedRegion(KittyCadBaseModel):
    """The region a user clicked on."""

    curve_clockwise: Optional[bool] = False

    intersection_index: Optional[int] = -1

    intersection_segment: str

    segment: str
