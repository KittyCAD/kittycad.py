
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d
from ..models.unit_length import UnitLength


class CenterOfMass(BaseModel):
    """The center of mass response."""

    center_of_mass: Point3d

    output_unit: UnitLength

    model_config = ConfigDict(protected_namespaces=())
