from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class RegionGetQueryPoint(KittyCadBaseModel):
    """The response from 'RegionGetQueryPoint' modeling command."""

    query_point: Point2d
