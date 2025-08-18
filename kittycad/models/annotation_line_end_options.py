from ..models.annotation_line_end import AnnotationLineEnd
from .base import KittyCadBaseModel


class AnnotationLineEndOptions(KittyCadBaseModel):
    """Options for annotation text"""

    end: AnnotationLineEnd

    start: AnnotationLineEnd
