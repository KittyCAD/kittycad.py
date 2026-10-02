from typing import Optional

from ..models.annotation_line_end import AnnotationLineEnd
from ..models.annotation_mbd_leader_position import AnnotationMbdLeaderPosition
from ..models.edge_specifier import EdgeSpecifier
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class AnnotationFeatureTag(KittyCadBaseModel):
    """Parameters for defining an MBD Feature Tag Annotation state"""

    edge_reference: Optional[EdgeSpecifier] = None

    entity_id: Optional[str] = None

    entity_leader_pos: Optional[AnnotationMbdLeaderPosition] = None

    entity_pos: Optional[Point2d] = None

    font_point_size: int

    font_scale: float

    key: str

    leader_scale: Optional[float] = 1.0

    leader_type: AnnotationLineEnd

    offset: Point2d

    plane_id: str

    show_key: bool

    value: str
