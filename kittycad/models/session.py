import datetime

from pydantic import BaseModel, ConfigDict



class Session(BaseModel):
    """An authentication session."""

    created_at: datetime.datetime

    expires_at: datetime.datetime

    token: str

    updated_at: datetime.datetime

    user_id: str

    model_config = ConfigDict(protected_namespaces=())
