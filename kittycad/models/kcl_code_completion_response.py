from typing import List

from .base import KittyCadBaseModel


class KclCodeCompletionResponse(KittyCadBaseModel):
    """A response with KCL code completions."""

    completions: List[str]
