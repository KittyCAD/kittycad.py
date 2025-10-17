from ..models.annotation_line_end import AnnotationLineEnd
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class AnnotationFeatureTag(KittyCadBaseModel):
    """Parameters for defining an MBD Feature Tag Annotation state"""

    entity_id: str

    entity_pos: Point2d

    font_point_size: int

    font_scale: float

    key: str

    leader_type: AnnotationLineEnd

    offset: Point2d

    plane_id: str

    show_key: bool

    value: str
