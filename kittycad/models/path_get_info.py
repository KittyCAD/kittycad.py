from typing import List

from pydantic import BaseModel

from ..models.path_segment_info import PathSegmentInfo


class PathGetInfo(BaseModel):
    """The response from the `PathGetInfo` command."""

    segments: List[PathSegmentInfo]
