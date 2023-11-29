from typing import Optional

from pydantic import BaseModel

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.path_command import PathCommand


class PathSegmentInfo(BaseModel):
    """Info about a path segment"""

    command: PathCommand

    command_id: Optional[ModelingCmdId] = None

    relative: bool
