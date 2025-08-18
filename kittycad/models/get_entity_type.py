from ..models.entity_type import EntityType
from .base import KittyCadBaseModel


class GetEntityType(KittyCadBaseModel):
    """The response from the `GetEntityType` command."""

    entity_type: EntityType
