from typing import List, Optional

from ..models.ml_prompt import MlPrompt
from .base import KittyCadBaseModel


class MlPromptResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[MlPrompt]

    next_page: Optional[str] = None
