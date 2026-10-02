from ..models.bounding_box import BoundingBox
from ..models.center_of_mass import CenterOfMass
from ..models.density import Density
from ..models.mass import Mass
from ..models.surface_area import SurfaceArea
from ..models.volume import Volume
from .base import KittyCadBaseModel


class PhysicalProperties(KittyCadBaseModel):
    """The physical properties response, containing the same data as the individual property responses."""

    bounding_box: BoundingBox

    center_of_mass: CenterOfMass

    density: Density

    mass: Mass

    surface_area: SurfaceArea

    volume: Volume
