import datetime

from pydantic import BaseModel

from ..models.uuid import Uuid


class Session(BaseModel):
    """An authentication session.

    For our UIs, these are automatically created by Next.js."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    session_token: Uuid

    updated_at: datetime.datetime

    user_id: Uuid
