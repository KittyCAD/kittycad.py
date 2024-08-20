from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.kcl_code_completion_params import KclCodeCompletionParams


class KclCodeCompletionRequest(BaseModel):
    """A request to generate KCL code completions."""

    extra: KclCodeCompletionParams = {"language": "", "trim_by_indentation": False}

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    nwo: Optional[str] = None

    prompt: str = ""

    stop: Optional[List[str]] = None

    stream: bool = False

    suffix: str = ""

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
