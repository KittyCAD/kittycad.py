import datetime
from typing import Optional

from pydantic import BaseModel

from ..models.uuid import Uuid


class VerificationToken(BaseModel):
    """A verification token for a user.

    This is typically used to verify a user's email address."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    identifier: Optional[str] = None

    updated_at: datetime.datetime
