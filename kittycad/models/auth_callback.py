from typing import Optional

from pydantic import BaseModel, ConfigDict



class AuthCallback(BaseModel):
    """The authentication callback from the OAuth 2.0 client. This is typically posted to the redirect URL as query params after authenticating."""

    code: Optional[str] = None

    id_token: Optional[str] = None

    state: Optional[str] = None

    user: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
