from ..models.source_position import SourcePosition
from .base import KittyCadBaseModel


class SourceRange(KittyCadBaseModel):
    """A source range of code."""

    end: SourcePosition

    start: SourcePosition
