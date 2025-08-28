import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class VerificationTokenResponse(KittyCadBaseModel):
    """A verification token response."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    identifier: Optional[str] = None

    redirect_url: Optional[str] = None

    updated_at: datetime.datetime
