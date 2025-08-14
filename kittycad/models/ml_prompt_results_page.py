from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.ml_prompt import MlPrompt


class MlPromptResultsPage(BaseModel):
    """A single page of results"""

    items: List[MlPrompt]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
