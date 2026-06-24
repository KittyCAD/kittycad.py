from typing import Optional

from ..models.annotation_mbd_basic_dimension import AnnotationMbdBasicDimension
from ..models.edge_specifier import EdgeSpecifier
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class AnnotationBasicDimension(KittyCadBaseModel):
    """Parameters for defining an MBD Basic Dimension Annotation state which is measured between two positions in 3D"""

    arrow_scale: Optional[float] = 1.0

    dimension: AnnotationMbdBasicDimension

    font_point_size: int

    font_scale: float

    from_edge_reference: Optional[EdgeSpecifier] = None

    from_entity_id: Optional[str] = None

    from_entity_pos: Point2d

    offset: Point2d

    plane_id: str

    precision: int

    to_edge_reference: Optional[EdgeSpecifier] = None

    to_entity_id: Optional[str] = None

    to_entity_pos: Point2d
