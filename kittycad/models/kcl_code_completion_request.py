from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.kcl_code_completion_params import KclCodeCompletionParams


class KclCodeCompletionRequest(BaseModel):
    """A request to generate KCL code completions."""

    extra: Optional[KclCodeCompletionParams] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    nwo: Optional[str] = None

    prompt: Optional[str] = None

    stop: Optional[List[str]] = None

    stream: Optional[bool] = None

    suffix: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
