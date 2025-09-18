from typing import List, Optional

from ..models.source_range_prompt import SourceRangePrompt
from .base import KittyCadBaseModel


class TextToCadIterationBody(KittyCadBaseModel):
    """Body for generating parts from text."""

    kcl_version: Optional[str] = None

    original_source_code: str

    project_name: Optional[str] = None

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]
