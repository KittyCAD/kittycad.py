from ..models.length_unit import LengthUnit
from .base import KittyCadBaseModel


class EntityGetDistance(KittyCadBaseModel):
    """The response from the `EntitiesGetDistance` command."""

    max_distance: LengthUnit

    min_distance: LengthUnit
