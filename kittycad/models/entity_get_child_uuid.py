from .base import KittyCadBaseModel


class EntityGetChildUuid(KittyCadBaseModel):
    """The response from the `EntityGetChildUuid` command."""

    entity_id: str
