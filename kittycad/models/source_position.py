from .base import KittyCadBaseModel


class SourcePosition(KittyCadBaseModel):
    """A position in the source code."""

    column: int

    line: int
