import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.path_command import PathCommand
from .base64data import Base64Data


class PathSegmentInfo(BaseModel):
    """Info about a path segment"""

    command: PathCommand

    command_id: Optional[ModelingCmdId] = None

    relative: bool

    model_config = ConfigDict(protected_namespaces=())
