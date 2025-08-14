from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.text_to_cad_response import TextToCadResponse


class TextToCadResponseResultsPage(BaseModel):
    """A single page of results"""

    items: List[TextToCadResponse]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
