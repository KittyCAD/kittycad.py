
from pydantic import BaseModel, ConfigDict

from ..models.annotation_text_alignment_x import AnnotationTextAlignmentX
from ..models.annotation_text_alignment_y import AnnotationTextAlignmentY


class AnnotationTextOptions(BaseModel):
    """Options for annotation text"""

    point_size: int

    text: str

    x: AnnotationTextAlignmentX

    y: AnnotationTextAlignmentY

    model_config = ConfigDict(protected_namespaces=())
