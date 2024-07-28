
from pydantic import BaseModel, ConfigDict

from ..models.unit_volume import UnitVolume


class Volume(BaseModel):
    """The volume response."""

    output_unit: UnitVolume

    volume: float

    model_config = ConfigDict(protected_namespaces=())
