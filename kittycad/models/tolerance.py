from ..models.length_unit import LengthUnit
from .base import KittyCadBaseModel


class Tolerance(KittyCadBaseModel):
    """Default tolerance values for modeling operations."""

    point_point_2d_coincident: LengthUnit
