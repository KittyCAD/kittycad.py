from typing import List

from ..models.curve_debug import CurveDebug
from .base import KittyCadBaseModel


class SketchGetInfo(KittyCadBaseModel):
    """The response from the 'SketchGetInfo'."""

    curves: List[CurveDebug]

    region_count: int

    region_obj: str
