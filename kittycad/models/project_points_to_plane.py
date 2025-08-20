from typing import List

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class ProjectPointsToPlane(KittyCadBaseModel):
    """The response from the `ProjectPointsToPlane` command."""

    projected_points: List[Point3d]
