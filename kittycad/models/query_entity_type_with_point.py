from typing import Optional

from ..models.entity_reference import EntityReference
from .base import KittyCadBaseModel


class QueryEntityTypeWithPoint(KittyCadBaseModel):
    """The response from the `QueryEntityTypeWithPoint` command."""

    reference: Optional[EntityReference] = None
