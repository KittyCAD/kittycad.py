from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.path_segment_info import PathSegmentInfo


class PathGetInfo(BaseModel):
    """The response from the `PathGetInfo` command."""

    segments: List[PathSegmentInfo]

    model_config = ConfigDict(protected_namespaces=())
