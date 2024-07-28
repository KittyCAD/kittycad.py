
from pydantic import BaseModel, ConfigDict

from ..models.unit_area import UnitArea


class SurfaceArea(BaseModel):
    """The surface area response."""

    output_unit: UnitArea

    surface_area: float

    model_config = ConfigDict(protected_namespaces=())
