import datetime

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


class Conversation(BaseModel):
    """A conversation composed of many ML prompts."""

    created_at: datetime.datetime

    first_prompt: str

    id: Uuid

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
