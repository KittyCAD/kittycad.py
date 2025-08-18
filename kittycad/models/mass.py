from ..models.unit_mass import UnitMass
from .base import KittyCadBaseModel


class Mass(KittyCadBaseModel):
    """The mass response."""

    mass: float

    output_unit: UnitMass
