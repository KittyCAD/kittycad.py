import datetime

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


class Session(BaseModel):
    """An authentication session."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    session_token: Uuid

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
