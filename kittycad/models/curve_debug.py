from typing import Optional

from ..models.curve_type_debug import CurveTypeDebug
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class CurveDebug(KittyCadBaseModel):
    """A debug-view of the segment of a curve."""

    center: Optional[Point2d] = None

    end: Optional[Point2d] = None

    id: ModelingCmdId

    mid: Optional[Point2d] = None

    segment_type: CurveTypeDebug

    start: Optional[Point2d] = None
