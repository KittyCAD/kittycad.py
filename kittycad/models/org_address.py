import datetime
from typing import Optional

from ..models.country_code import CountryCode
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgAddress(KittyCadBaseModel):
    """An address for an organization."""

    city: Optional[str] = None

    country: CountryCode

    created_at: datetime.datetime

    id: Uuid

    org_id: Uuid

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    updated_at: datetime.datetime

    zip: Optional[str] = None
