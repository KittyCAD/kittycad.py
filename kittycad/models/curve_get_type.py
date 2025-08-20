from ..models.curve_type import CurveType
from .base import KittyCadBaseModel


class CurveGetType(KittyCadBaseModel):
    """The response from the `CurveGetType` command."""

    curve_type: CurveType
