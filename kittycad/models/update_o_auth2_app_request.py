from .base import KittyCadBaseModel


class UpdateOAuth2AppRequest(KittyCadBaseModel):
    """Request body for updating a public device-flow app."""

    name: str
