from .base import KittyCadBaseModel


class RegionGetResolvableIntersectionInfo(KittyCadBaseModel):
    """The response from the 'RegionGetResolvableIntersectionInfo'."""

    curve_clockwise: bool

    intersection_count: int

    intersection_index: int

    intersection_segment: str

    segment: str
