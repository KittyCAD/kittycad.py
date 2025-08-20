from ..models.point3d import Point3d
from ..models.unit_length import UnitLength
from .base import KittyCadBaseModel


class CenterOfMass(KittyCadBaseModel):
    """The center of mass response."""

    center_of_mass: Point3d

    output_unit: UnitLength
