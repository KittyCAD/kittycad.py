from ..models.unit_angle import UnitAngle
from .base import KittyCadBaseModel


class Angle(KittyCadBaseModel):
    """An angle, with a specific unit."""

    unit: UnitAngle

    value: float
