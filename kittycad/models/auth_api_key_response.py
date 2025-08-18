from .base import KittyCadBaseModel


class AuthApiKeyResponse(KittyCadBaseModel):
    """The response from the `/auth/api-key` endpoint."""

    session_token: str
