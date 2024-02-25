from typing import List

from pydantic import BaseModel, ConfigDict



class KclCodeCompletionResponse(BaseModel):
    """A response with KCL code completions."""

    completions: List[str]

    model_config = ConfigDict(protected_namespaces=())
