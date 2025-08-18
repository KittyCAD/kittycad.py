from typing import Optional

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.path_command import PathCommand
from .base import KittyCadBaseModel


class PathSegmentInfo(KittyCadBaseModel):
    """Info about a path segment"""

    command: PathCommand

    command_id: Optional[ModelingCmdId] = None

    relative: bool
