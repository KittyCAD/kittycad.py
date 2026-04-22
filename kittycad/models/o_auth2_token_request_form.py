from typing import Optional

from ..models.o_auth2_authorization_code_uuid import OAuth2AuthorizationCodeUuid
from ..models.o_auth2_refresh_token_uuid import OAuth2RefreshTokenUuid
from ..models.o_auth2_token_grant_type import OAuth2TokenGrantType
from .base import KittyCadBaseModel


class OAuth2TokenRequestForm(KittyCadBaseModel):
    """Form body for `/oauth2/token`."""

    client_id: str

    code: Optional[OAuth2AuthorizationCodeUuid] = None

    code_verifier: Optional[str] = None

    grant_type: OAuth2TokenGrantType

    redirect_uri: Optional[str] = None

    refresh_token: Optional[OAuth2RefreshTokenUuid] = None
