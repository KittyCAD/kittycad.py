from typing import List, Optional

from ..models.source_range_prompt import SourceRangePrompt
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class TextToCadMultiFileIterationBody(KittyCadBaseModel):
    """Body for iterating on models from text prompts."""

    conversation_id: Optional[Uuid] = None

    kcl_version: Optional[str] = None

    project_name: Optional[str] = None

    prompt: Optional[str] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None
