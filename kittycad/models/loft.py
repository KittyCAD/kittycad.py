from .base import KittyCadBaseModel


class Loft(KittyCadBaseModel):
    """The response from the `Loft` command."""

    solid_id: str
