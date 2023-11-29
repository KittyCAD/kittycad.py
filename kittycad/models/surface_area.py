
from pydantic import BaseModel

from ..models.unit_area import UnitArea


class SurfaceArea(BaseModel):
    """The surface area response."""

    output_unit: UnitArea

    surface_area: float
