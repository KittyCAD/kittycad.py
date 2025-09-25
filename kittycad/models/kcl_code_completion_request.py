from typing import List, Optional

from ..models.kcl_code_completion_params import KclCodeCompletionParams
from .base import KittyCadBaseModel


class KclCodeCompletionRequest(KittyCadBaseModel):
    """A request to generate KCL code completions."""

    extra: KclCodeCompletionParams = {"language": "", "trim_by_indentation": False}  # type: ignore[assignment]

    max_tokens: Optional[int] = None

    model_version: Optional[str] = None

    n: Optional[int] = None

    nwo: Optional[str] = None

    prompt: str = ""

    stop: Optional[List[str]] = None

    stream: bool = False

    suffix: str = ""

    temperature: Optional[float] = None

    top_p: Optional[float] = None
