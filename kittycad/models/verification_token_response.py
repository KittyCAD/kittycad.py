import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.uuid import Uuid
from .base64data import Base64Data


class VerificationTokenResponse(BaseModel):
    """A verification token response."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    identifier: Optional[str] = None

    saml_redirect_url: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
