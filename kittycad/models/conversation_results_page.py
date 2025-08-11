from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.conversation import Conversation


class ConversationResultsPage(BaseModel):
    """A single page of results"""

    items: List[Conversation]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
