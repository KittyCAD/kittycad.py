from .base import KittyCadBaseModel


class EntityGetNumChildren(KittyCadBaseModel):
    """The response from the `EntityGetNumChildren` command."""

    num: int
