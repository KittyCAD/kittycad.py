
from pydantic import BaseModel

from ..models.unit_density import UnitDensity


class Density(BaseModel):
    """The density response."""

    density: float

    output_unit: UnitDensity
