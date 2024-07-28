from typing import Optional

from pydantic import BaseModel, ConfigDict



class OAuth2ClientInfo(BaseModel):
    """Information about an OAuth 2.0 client."""

    csrf_token: Optional[str] = None

    pkce_code_verifier: Optional[str] = None

    url: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
