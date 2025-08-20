from typing import Optional

from .base import KittyCadBaseModel


class OAuth2ClientInfo(KittyCadBaseModel):
    """Information about an OAuth 2.0 client."""

    csrf_token: Optional[str] = None

    oidc_nonce: Optional[str] = None

    pkce_code_verifier: Optional[str] = None

    url: Optional[str] = None
