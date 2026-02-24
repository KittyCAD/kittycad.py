import datetime
from typing import Optional

from ..models.email_marketing_consent_status import EmailMarketingConsentStatus
from .base import KittyCadBaseModel


class EmailMarketingConsentState(KittyCadBaseModel):
    """Public view of an authenticated user's email marketing consent state."""

    confirmed_at: Optional[datetime.datetime] = None

    is_subscribed: bool

    prompt_seen_at: Optional[datetime.datetime] = None

    requested_at: Optional[datetime.datetime] = None

    should_show_prompt: bool

    status: EmailMarketingConsentStatus
