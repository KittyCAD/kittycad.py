
from pydantic import BaseModel, ConfigDict

from ..models.o_auth2_grant_type import OAuth2GrantType


class DeviceAccessTokenRequestForm(BaseModel):
    """The form for a device access token request."""

    client_id: str

    device_code: str

    grant_type: OAuth2GrantType

    model_config = ConfigDict(protected_namespaces=())
