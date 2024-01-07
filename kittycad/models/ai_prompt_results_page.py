from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.ai_prompt import AiPrompt


class AiPromptResultsPage(BaseModel):
    """A single page of results"""

    items: List[AiPrompt]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
