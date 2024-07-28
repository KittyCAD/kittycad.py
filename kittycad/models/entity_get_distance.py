
from pydantic import BaseModel, ConfigDict

from ..models.length_unit import LengthUnit


class EntityGetDistance(BaseModel):
    """The response from the `EntitiesGetDistance` command."""

    max_distance: LengthUnit

    min_distance: LengthUnit

    model_config = ConfigDict(protected_namespaces=())
