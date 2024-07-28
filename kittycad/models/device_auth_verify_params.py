import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class DeviceAuthVerifyParams(BaseModel):
    """The request parameters to verify the `user_code` for the OAuth 2.0 Device Authorization Grant."""

    user_code: str

    model_config = ConfigDict(protected_namespaces=())
