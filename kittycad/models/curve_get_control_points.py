from typing import List

from pydantic import BaseModel

from ..models.point3d import Point3d


class CurveGetControlPoints(BaseModel):
    """The response from the `CurveGetControlPoints` command."""

    control_points: List[Point3d]
