from pydantic import BaseModel, ConfigDict

from ..models.angle import Angle
from ..models.origin_type import OriginType
from ..models.point3d import Point3d


class Rotation(BaseModel):
    """A rotation defined by an axis, origin of rotation, and an angle."""

    angle: Angle

    axis: Point3d

    origin: OriginType

    model_config = ConfigDict(protected_namespaces=())
