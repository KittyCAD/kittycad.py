from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.origin_type import OriginType
from ..models.point4d import Point4d


class TransformByForPoint4d(BaseModel):
    """How a property of an object should be transformed."""

    is_local: bool

    origin: Optional[OriginType] = None

    property: Point4d

    set: bool

    model_config = ConfigDict(protected_namespaces=())
