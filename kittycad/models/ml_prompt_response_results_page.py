from typing import List, Optional

from ..models.ml_prompt_response import MlPromptResponse
from .base import KittyCadBaseModel


class MlPromptResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[MlPromptResponse]

    next_page: Optional[str] = None
