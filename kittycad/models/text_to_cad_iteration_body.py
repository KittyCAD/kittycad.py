from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.source_range_prompt import SourceRangePrompt


class TextToCadIterationBody(BaseModel):
    """Body for generating models from text."""

    original_source_code: str

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]

    model_config = ConfigDict(protected_namespaces=())
