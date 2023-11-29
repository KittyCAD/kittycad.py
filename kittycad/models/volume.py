
from pydantic import BaseModel

from ..models.unit_volume import UnitVolume


class Volume(BaseModel):
    """The volume response."""

    output_unit: UnitVolume

    volume: float
