from typing import Optional

from ..models.country_code import CountryCode
from .base import KittyCadBaseModel


class AddressDetails(KittyCadBaseModel):
    """Address details."""

    city: Optional[str] = None

    country: CountryCode

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    zip: Optional[str] = None
