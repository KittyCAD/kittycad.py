import datetime
from typing import Optional

from ..models.block_reason import BlockReason
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ExtendedUser(KittyCadBaseModel):
    """Extended user information.

    This is mostly used for internal purposes. It returns a mapping of the user's information, including that of our third party services we use for users: Stripe"""

    block: Optional[BlockReason] = None

    can_train_on_data: Optional[bool] = False

    company: Optional[str] = None

    created_at: datetime.datetime

    deletion_scheduled: Optional[bool] = False

    discord: Optional[str] = None

    email: Optional[str] = None

    email_verified: Optional[datetime.datetime] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    hubspot_contact_id: Optional[str] = None

    id: Uuid

    image: str

    is_onboarded: Optional[bool] = False

    is_service_account: Optional[bool] = False

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = ""

    stripe_id: Optional[str] = None

    updated_at: datetime.datetime
