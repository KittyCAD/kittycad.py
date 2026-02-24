from ..models.origin_type import OriginType
from ..models.point4d import Point4d
from .base import KittyCadBaseModel


class TransformByForPoint4d(KittyCadBaseModel):
    """How a property of an object should be transformed."""

    origin: OriginType = {"type": "local"}  # type: ignore[assignment]

    property: Point4d

    set: bool
