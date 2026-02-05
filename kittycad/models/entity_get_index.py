from .base import KittyCadBaseModel


class EntityGetIndex(KittyCadBaseModel):
    """The response from the `EntityGetIndex` command."""

    entity_index: int
