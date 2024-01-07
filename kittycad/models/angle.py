
from pydantic import BaseModel, ConfigDict

from ..models.unit_angle import UnitAngle


class Angle(BaseModel):
    """An angle, with a specific unit."""

    unit: UnitAngle

    value: float

    model_config = ConfigDict(protected_namespaces=())
