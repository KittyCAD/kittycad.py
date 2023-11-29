
from pydantic import BaseModel

from ..models.annotation_line_end import AnnotationLineEnd


class AnnotationLineEndOptions(BaseModel):
    """Options for annotation text"""

    end: AnnotationLineEnd

    start: AnnotationLineEnd
