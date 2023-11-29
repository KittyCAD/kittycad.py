
from pydantic import BaseModel

from ..models.unit_angle import UnitAngle


class Angle(BaseModel):
    """An angle, with a specific unit."""

    unit: UnitAngle

    value: float
