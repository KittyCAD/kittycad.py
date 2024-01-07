
from pydantic import BaseModel, ConfigDict

from ..models.unit_mass import UnitMass


class Mass(BaseModel):
    """The mass response."""

    mass: float

    output_unit: UnitMass

    model_config = ConfigDict(protected_namespaces=())
