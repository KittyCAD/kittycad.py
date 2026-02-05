from ..models.entity_type import EntityType
from .base import KittyCadBaseModel


class EntityGetPrimitiveIndex(KittyCadBaseModel):
    """The response from the `EntityGetPrimitiveIndex` command."""

    entity_type: EntityType

    primitive_index: int
