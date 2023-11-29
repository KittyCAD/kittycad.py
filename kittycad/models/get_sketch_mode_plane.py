
from pydantic import BaseModel

from ..models.point3d import Point3d


class GetSketchModePlane(BaseModel):
    """The plane for sketch mode."""

    x_axis: Point3d

    y_axis: Point3d

    z_axis: Point3d
