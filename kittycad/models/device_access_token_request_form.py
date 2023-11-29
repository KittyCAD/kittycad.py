from uuid import UUID

from pydantic import BaseModel

from ..models.o_auth2_grant_type import OAuth2GrantType


class DeviceAccessTokenRequestForm(BaseModel):
    """The form for a device access token request."""

    client_id: UUID

    device_code: UUID

    grant_type: OAuth2GrantType
