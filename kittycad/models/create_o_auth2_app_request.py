from .base import KittyCadBaseModel


class CreateOAuth2AppRequest(KittyCadBaseModel):
    """Request body for creating a public device-flow app."""

    name: str
