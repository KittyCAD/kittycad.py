from pydantic import BaseModel, ConfigDict

from ..models.source_position import SourcePosition


class Sourcerange(BaseModel):
    """A source range of code."""

    end: SourcePosition

    start: SourcePosition

    model_config = ConfigDict(protected_namespaces=())
