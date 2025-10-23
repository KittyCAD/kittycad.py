import datetime
from typing import Optional

from ..models.country_code import CountryCode
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class Address(KittyCadBaseModel):
    """An address for a user."""

    city: Optional[str] = None

    country: CountryCode

    created_at: datetime.datetime

    id: Uuid

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    updated_at: datetime.datetime

    user_id: Uuid

    zip: Optional[str] = None
