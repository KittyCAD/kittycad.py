from ..models.angle import Angle
from ..models.origin_type import OriginType
from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class Rotation(KittyCadBaseModel):
    """A rotation defined by an axis, origin of rotation, and an angle."""

    angle: Angle

    axis: Point3d

    origin: OriginType
