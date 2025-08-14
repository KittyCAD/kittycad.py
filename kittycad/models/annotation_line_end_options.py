from pydantic import BaseModel, ConfigDict

from ..models.annotation_line_end import AnnotationLineEnd


class Annotationlineendoptions(BaseModel):
    """Options for annotation text"""

    end: AnnotationLineEnd

    start: AnnotationLineEnd

    model_config = ConfigDict(protected_namespaces=())
