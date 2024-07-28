
from pydantic import BaseModel, ConfigDict

from ..models.length_unit import LengthUnit


class Point2d(BaseModel):
    """A point in 2D space"""

    x: LengthUnit

    y: LengthUnit

    model_config = ConfigDict(protected_namespaces=())
