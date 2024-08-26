from typing import Optional

from pydantic import BaseModel, ConfigDict



class TokenRevokeRequestForm(BaseModel):
    """The request parameters for the OAuth 2.0 token revocation flow."""

    client_id: str

    client_secret: Optional[str] = None

    token: str

    model_config = ConfigDict(protected_namespaces=())
