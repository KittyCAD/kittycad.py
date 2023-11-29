import datetime
from typing import Optional

from pydantic import BaseModel

from ..models.uuid import Uuid


class ExtendedUser(BaseModel):
    """Extended user information.

    This is mostly used for internal purposes. It returns a mapping of the user's information, including that of our third party services we use for users: MailChimp, Stripe, and Front
    """

    company: Optional[str] = None

    created_at: datetime.datetime

    discord: Optional[str] = None

    email: Optional[str] = None

    email_verified: Optional[datetime.datetime] = None

    first_name: Optional[str] = None

    front_id: Optional[str] = None

    github: Optional[str] = None

    id: Uuid

    image: str

    last_name: Optional[str] = None

    mailchimp_id: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    stripe_id: Optional[str] = None

    updated_at: datetime.datetime
