from .base import KittyCadBaseModel


class SelectedRegion(KittyCadBaseModel):
    """The region a user clicked on."""

    curve_clockwise: bool = False

    intersection_index: int = -1

    intersection_segment: str

    segment: str
