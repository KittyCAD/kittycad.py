import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.block_reason import BlockReason
from ..models.uuid import Uuid
from .base64data import Base64Data


class ExtendedUser(BaseModel):
    """Extended user information.

    This is mostly used for internal purposes. It returns a mapping of the user's information, including that of our third party services we use for users: MailChimp | Stripe
    """

    block: Optional[BlockReason] = None

    can_train_on_data: Optional[bool] = None

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

    is_service_account: Optional[bool] = None

    last_name: Optional[str] = None

    mailchimp_id: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    stripe_id: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
