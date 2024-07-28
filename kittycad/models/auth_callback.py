import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class AuthCallback(BaseModel):
    """The authentication callback from the OAuth 2.0 client. This is typically posted to the redirect URL as query params after authenticating."""

    code: Optional[str] = None

    id_token: Optional[str] = None

    state: Optional[str] = None

    user: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
