from ..models.unit_volume import UnitVolume
from .base import KittyCadBaseModel


class Volume(KittyCadBaseModel):
    """The volume response."""

    output_unit: UnitVolume

    volume: float
