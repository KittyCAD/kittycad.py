import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.string_uuid import StringUuid
from ..models.uuid import Uuid
from .base64data import Base64Data


class ApiToken(BaseModel):
    """An API token.

    These are used to authenticate users with Bearer authentication."""

    created_at: datetime.datetime

    id: Uuid

    is_valid: bool

    label: Optional[str] = None

    token: StringUuid

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
