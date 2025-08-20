from .base import KittyCadBaseModel


class EntityGetParentId(KittyCadBaseModel):
    """The response from the `EntityGetParentId` command."""

    entity_id: str
