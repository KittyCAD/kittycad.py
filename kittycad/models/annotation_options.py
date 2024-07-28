import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.annotation_line_end_options import AnnotationLineEndOptions
from ..models.annotation_text_options import AnnotationTextOptions
from ..models.color import Color
from ..models.point3d import Point3d
from .base64data import Base64Data


class AnnotationOptions(BaseModel):
    """Options for annotations"""

    color: Optional[Color] = None

    line_ends: Optional[AnnotationLineEndOptions] = None

    line_width: Optional[float] = None

    position: Optional[Point3d] = None

    text: Optional[AnnotationTextOptions] = None

    model_config = ConfigDict(protected_namespaces=())
