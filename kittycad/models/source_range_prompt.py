from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.source_range import SourceRange


class SourceRangePrompt(BaseModel):
    """A source range and prompt for a text to CAD iteration."""

    file: Optional[str] = None

    prompt: str

    range: SourceRange

    model_config = ConfigDict(protected_namespaces=())
