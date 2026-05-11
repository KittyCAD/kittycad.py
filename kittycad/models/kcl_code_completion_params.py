from typing import Optional

from .base import KittyCadBaseModel


class KclCodeCompletionParams(KittyCadBaseModel):
    """Extra params for the completions."""

    language: Optional[str] = ""

    next_indent: Optional[int] = None

    prompt_tokens: Optional[int] = None

    suffix_tokens: Optional[int] = None

    trim_by_indentation: Optional[bool] = False
