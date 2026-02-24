from ..models.origin_type import OriginType
from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class TransformByForPoint3d(KittyCadBaseModel):
    """How a property of an object should be transformed."""

    origin: OriginType = {"type": "local"}  # type: ignore[assignment]

    property: Point3d

    set: bool
