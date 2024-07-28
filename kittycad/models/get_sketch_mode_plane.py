
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class GetSketchModePlane(BaseModel):
    """The plane for sketch mode."""

    origin: Point3d

    x_axis: Point3d

    y_axis: Point3d

    z_axis: Point3d

    model_config = ConfigDict(protected_namespaces=())
