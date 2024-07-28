import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.annotation_text_alignment_x import AnnotationTextAlignmentX
from ..models.annotation_text_alignment_y import AnnotationTextAlignmentY
from .base64data import Base64Data


class AnnotationTextOptions(BaseModel):
    """Options for annotation text"""

    point_size: int

    text: str

    x: AnnotationTextAlignmentX

    y: AnnotationTextAlignmentY

    model_config = ConfigDict(protected_namespaces=())
