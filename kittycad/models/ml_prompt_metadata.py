from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.source_range_prompt import SourceRangePrompt


class MlPromptMetadata(BaseModel):
    """Metadata for a ML prompt."""

    code: Optional[str] = None

    original_source_code: Optional[str] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None

    model_config = ConfigDict(protected_namespaces=())
