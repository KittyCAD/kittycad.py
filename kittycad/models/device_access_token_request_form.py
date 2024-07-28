import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.o_auth2_grant_type import OAuth2GrantType
from .base64data import Base64Data


class DeviceAccessTokenRequestForm(BaseModel):
    """The form for a device access token request."""

    client_id: str

    device_code: str

    grant_type: OAuth2GrantType

    model_config = ConfigDict(protected_namespaces=())
