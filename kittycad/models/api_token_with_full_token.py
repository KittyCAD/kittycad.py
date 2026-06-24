import datetime
from typing import Optional

from ..models.api_token_uuid import ApiTokenUuid
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ApiTokenWithFullToken(KittyCadBaseModel):
    """An API token with the full, unobfuscated token value.

    This is used specifically for the creation endpoint response, where the user needs to see the full token exactly once. All other endpoints return the obfuscated version via the `ApiToken` struct."""

    created_at: datetime.datetime

    id: Uuid

    is_valid: bool

    label: Optional[str] = None

    token: ApiTokenUuid

    updated_at: datetime.datetime

    user_id: Uuid
