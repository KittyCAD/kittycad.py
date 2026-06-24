from ..models.length_unit import LengthUnit
from .base import KittyCadBaseModel


class EdgeGetLength(KittyCadBaseModel):
    """The response from the `EdgeGetLength` command."""

    length: LengthUnit
