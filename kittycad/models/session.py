import datetime

from ..models.session_uuid import SessionUuid
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class Session(KittyCadBaseModel):
    """An authentication session."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    session_token: SessionUuid

    updated_at: datetime.datetime

    user_id: Uuid
