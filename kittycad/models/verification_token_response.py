import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


class VerificationTokenResponse(BaseModel):
    """A verification token response."""

    created_at: datetime.datetime

    expires: datetime.datetime

    id: Uuid

    identifier: Optional[str] = None

    saml_redirect_url: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
