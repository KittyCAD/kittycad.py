from typing import Optional

from .base import KittyCadBaseModel


class AuthCallback(KittyCadBaseModel):
    """The authentication callback from the OAuth 2.0 client. This is typically posted to the redirect URL as query params after authenticating."""

    code: Optional[str] = None

    id_token: Optional[str] = None

    state: Optional[str] = None

    user: Optional[str] = None
