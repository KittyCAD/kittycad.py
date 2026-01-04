from ..models.annotation_mbd_basic_dimension import AnnotationMbdBasicDimension
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class AnnotationBasicDimension(KittyCadBaseModel):
    """Parameters for defining an MBD Basic Dimension Annotation state which is measured between two positions in 3D"""

    dimension: AnnotationMbdBasicDimension

    font_point_size: int

    font_scale: float

    from_entity_id: str

    from_entity_pos: Point2d

    offset: Point2d

    plane_id: str

    precision: int

    to_entity_id: str

    to_entity_pos: Point2d
