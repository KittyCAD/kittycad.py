from typing import List

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class ProjectEntityToPlane(KittyCadBaseModel):
    """The response from the `ProjectEntityToPlane` command."""

    projected_points: List[Point3d]
