from ..models.oauth2_grant_type import OAuth2GrantType
from .base import KittyCadBaseModel


class DeviceAccessTokenRequestForm(KittyCadBaseModel):
    """The form for a device access token request."""

    client_id: str

    device_code: str

    grant_type: OAuth2GrantType
