from ..models.unit_density import UnitDensity
from .base import KittyCadBaseModel


class Density(KittyCadBaseModel):
    """The density response."""

    density: float

    output_unit: UnitDensity
