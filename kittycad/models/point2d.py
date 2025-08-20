from ..models.length_unit import LengthUnit
from .base import KittyCadBaseModel


class Point2d(KittyCadBaseModel):
    """A point in 2D space"""

    x: LengthUnit

    y: LengthUnit
