from typing import Optional

from ..models.annotation_basic_dimension import AnnotationBasicDimension
from ..models.annotation_feature_control import AnnotationFeatureControl
from ..models.annotation_feature_tag import AnnotationFeatureTag
from ..models.annotation_line_end_options import AnnotationLineEndOptions
from ..models.annotation_text_options import AnnotationTextOptions
from ..models.color import Color
from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class AnnotationOptions(KittyCadBaseModel):
    """Options for annotations"""

    color: Optional[Color] = None

    dimension: Optional[AnnotationBasicDimension] = None

    feature_control: Optional[AnnotationFeatureControl] = None

    feature_tag: Optional[AnnotationFeatureTag] = None

    line_ends: Optional[AnnotationLineEndOptions] = None

    line_width: Optional[float] = None

    position: Optional[Point3d] = None

    text: Optional[AnnotationTextOptions] = None
