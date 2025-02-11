from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.source_range_prompt import SourceRangePrompt


class TextToCadMultiFileIterationBody(BaseModel):
    """Body for generating models from text."""

    source_ranges: List[SourceRangePrompt]

    model_config = ConfigDict(protected_namespaces=())
