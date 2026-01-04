import datetime

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class CustomModel(KittyCadBaseModel):
    """Custom ML model created by a user for an organization."""

    created_at: datetime.datetime

    id: Uuid

    name: str

    org_id: Uuid

    system_prompt: str

    updated_at: datetime.datetime
