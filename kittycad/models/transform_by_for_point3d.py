from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.origin_type import OriginType
from ..models.point3d import Point3d


class TransformByForPoint3d(BaseModel):
    """How a property of an object should be transformed."""

    is_local: bool

    origin: Optional[OriginType] = None

    property: Point3d

    set: bool

    model_config = ConfigDict(protected_namespaces=())
