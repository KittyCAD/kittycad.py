import datetime

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class Conversation(KittyCadBaseModel):
    """A conversation composed of many ML prompts."""

    created_at: datetime.datetime

    first_prompt: str

    id: Uuid

    updated_at: datetime.datetime

    user_id: Uuid
