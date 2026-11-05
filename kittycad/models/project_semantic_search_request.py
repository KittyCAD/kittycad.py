from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectSemanticSearchRequest(KittyCadBaseModel):
    """Natural-language search within the caller's current organization library."""

    library_id: Optional[Uuid] = None

    limit: Optional[int] = None

    q: str
