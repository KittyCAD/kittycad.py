from typing import Optional

from pydantic import BaseModel, ConfigDict



class KclCodeCompletionParams(BaseModel):
    """Extra params for the completions."""

    language: str = ""

    next_indent: Optional[int] = None

    prompt_tokens: Optional[int] = None

    suffix_tokens: Optional[int] = None

    trim_by_indentation: bool = False

    model_config = ConfigDict(protected_namespaces=())
