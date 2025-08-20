from typing import List, Optional

from ..models.conversation import Conversation
from .base import KittyCadBaseModel


class ConversationResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[Conversation]

    next_page: Optional[str] = None
