from typing import Optional

from ..models.annotation_line_end import AnnotationLineEnd
from ..models.annotation_mbd_basic_dimension import AnnotationMbdBasicDimension
from ..models.annotation_mbd_control_frame import AnnotationMbdControlFrame
from ..models.edge_specifier import EdgeSpecifier
from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class AnnotationFeatureControl(KittyCadBaseModel):
    """Parameters for defining an MBD Feature Control Annotation state"""

    control_frame: Optional[AnnotationMbdControlFrame] = None

    defined_datum: Optional[str] = None

    dimension: Optional[AnnotationMbdBasicDimension] = None

    edge_reference: Optional[EdgeSpecifier] = None

    entity_id: Optional[str] = None

    entity_pos: Point2d

    font_point_size: int

    font_scale: float

    leader_scale: Optional[float] = 1.0

    leader_type: AnnotationLineEnd

    offset: Point2d

    plane_id: str

    precision: int

    prefix: Optional[str] = None

    suffix: Optional[str] = None
