from ..models.unit_area import UnitArea
from .base import KittyCadBaseModel


class SurfaceArea(KittyCadBaseModel):
    """The surface area response."""

    output_unit: UnitArea

    surface_area: float
