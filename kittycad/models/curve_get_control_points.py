from typing import List

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class CurveGetControlPoints(KittyCadBaseModel):
    """The response from the `CurveGetControlPoints` command."""

    control_points: List[Point3d]
