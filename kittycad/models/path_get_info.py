from typing import List

from ..models.path_segment_info import PathSegmentInfo
from .base import KittyCadBaseModel


class PathGetInfo(KittyCadBaseModel):
    """The response from the `PathGetInfo` command."""

    segments: List[PathSegmentInfo]
