from .base import KittyCadBaseModel


class PublicProjectOwnerResponse(KittyCadBaseModel):
    """Public creator metadata for community project listings."""

    username: str
