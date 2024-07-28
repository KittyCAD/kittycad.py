import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.session_token_uuid import SessionTokenUuid
from ..models.uuid import Uuid
from .base64data import Base64Data


class Session(BaseModel):
    """An authentication session."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    session_token: SessionTokenUuid

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
