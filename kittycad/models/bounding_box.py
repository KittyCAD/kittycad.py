from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class BoundingBox(KittyCadBaseModel):
    """The response from the 'BoundingBox'."""

    center: Point3d

    dimensions: Point3d
