
from pydantic import BaseModel, ConfigDict

from ..models.unit_density import UnitDensity


class Density(BaseModel):
    """The density response."""

    density: float

    output_unit: UnitDensity

    model_config = ConfigDict(protected_namespaces=())
