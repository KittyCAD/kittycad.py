from typing import List, Optional

from ..models.text_to_cad_response import TextToCadResponse
from .base import KittyCadBaseModel


class TextToCadResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[TextToCadResponse]

    next_page: Optional[str] = None
