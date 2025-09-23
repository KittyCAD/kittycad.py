from typing import List, Optional

from ..models.source_range_prompt import SourceRangePrompt
from .base import KittyCadBaseModel


class MlPromptMetadata(KittyCadBaseModel):
    """Metadata for a ML prompt."""

    code: Optional[str] = None

    original_source_code: Optional[str] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None

    upstream_conversation_id: Optional[str] = None
