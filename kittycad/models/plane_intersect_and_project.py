from typing import Optional

from pydantic import BaseModel

from ..models.point2d import Point2d


class PlaneIntersectAndProject(BaseModel):
    """Corresponding coordinates of given window coordinates, intersected on given plane."""

    plane_coordinates: Optional[Point2d] = None
