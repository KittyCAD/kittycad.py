import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.path_segment_info import PathSegmentInfo
from .base64data import Base64Data


class PathGetInfo(BaseModel):
    """The response from the `PathGetInfo` command."""

    segments: List[PathSegmentInfo]

    model_config = ConfigDict(protected_namespaces=())
