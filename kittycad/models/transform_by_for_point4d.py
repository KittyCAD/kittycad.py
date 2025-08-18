from typing import Optional

from ..models.origin_type import OriginType
from ..models.point4d import Point4d
from .base import KittyCadBaseModel


class TransformByForPoint4d(KittyCadBaseModel):
    """How a property of an object should be transformed."""

    is_local: bool

    origin: Optional[OriginType] = None

    property: Point4d

    set: bool
