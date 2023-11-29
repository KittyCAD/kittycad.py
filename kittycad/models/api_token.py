import datetime

from pydantic import BaseModel

from ..models.uuid import Uuid


class ApiToken(BaseModel):
    """An API token.

    These are used to authenticate users with Bearer authentication."""

    created_at: datetime.datetime

    id: Uuid

    is_valid: bool

    token: Uuid

    updated_at: datetime.datetime

    user_id: Uuid
