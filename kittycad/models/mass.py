
from pydantic import BaseModel

from ..models.unit_mass import UnitMass


class Mass(BaseModel):
    """The mass response."""

    mass: float

    output_unit: UnitMass
