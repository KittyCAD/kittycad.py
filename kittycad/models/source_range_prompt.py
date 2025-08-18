from typing import Optional

from ..models.source_range import SourceRange
from .base import KittyCadBaseModel


class SourceRangePrompt(KittyCadBaseModel):
    """A source range and prompt for a text to CAD iteration."""

    file: Optional[str] = None

    prompt: str

    range: SourceRange
