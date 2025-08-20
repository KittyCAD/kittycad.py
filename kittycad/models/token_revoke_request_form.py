from typing import Optional

from ..models.device_access_token_uuid import DeviceAccessTokenUuid
from .base import KittyCadBaseModel


class TokenRevokeRequestForm(KittyCadBaseModel):
    """The request parameters for the OAuth 2.0 token revocation flow."""

    client_id: str

    client_secret: Optional[str] = None

    token: DeviceAccessTokenUuid
