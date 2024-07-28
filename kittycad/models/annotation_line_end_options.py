import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.annotation_line_end import AnnotationLineEnd
from .base64data import Base64Data


class AnnotationLineEndOptions(BaseModel):
    """Options for annotation text"""

    end: AnnotationLineEnd

    start: AnnotationLineEnd

    model_config = ConfigDict(protected_namespaces=())
