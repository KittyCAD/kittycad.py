from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.text_to_cad import TextToCad


class TextToCadResultsPage(BaseModel):
    """A single page of results"""

    items: List[TextToCad]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
