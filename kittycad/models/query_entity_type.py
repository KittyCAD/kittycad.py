from ..models.entity_reference import EntityReference
from .base import KittyCadBaseModel


class QueryEntityType(KittyCadBaseModel):
    """The response from the `QueryEntityType` command."""

    reference: EntityReference
