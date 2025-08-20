from ..models.annotation_text_alignment_x import AnnotationTextAlignmentX
from ..models.annotation_text_alignment_y import AnnotationTextAlignmentY
from .base import KittyCadBaseModel


class AnnotationTextOptions(KittyCadBaseModel):
    """Options for annotation text"""

    point_size: int

    text: str

    x: AnnotationTextAlignmentX

    y: AnnotationTextAlignmentY
