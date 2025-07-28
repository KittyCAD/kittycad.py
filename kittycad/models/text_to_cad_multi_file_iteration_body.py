from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.source_range_prompt import SourceRangePrompt
from ..models.uuid import Uuid


class TextToCadMultiFileIterationBody(BaseModel):
    """Body for iterating on models from text prompts."""

    conversation_id: Optional[Uuid] = None

    kcl_version: Optional[str] = None

    project_name: Optional[str] = None

    prompt: Optional[str] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None

    model_config = ConfigDict(protected_namespaces=())
