from typing import Optional

from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class PlaneIntersectAndProject(KittyCadBaseModel):
    """Corresponding coordinates of given window coordinates, intersected on given plane."""

    plane_coordinates: Optional[Point2d] = None
