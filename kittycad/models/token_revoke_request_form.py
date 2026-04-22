from typing import Optional

from .base import KittyCadBaseModel


class TokenRevokeRequestForm(KittyCadBaseModel):
    """The request parameters for the OAuth 2.0 token revocation flow."""

    client_id: str

    client_secret: Optional[str] = None

    token: str
