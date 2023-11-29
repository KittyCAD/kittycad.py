from typing import Optional

from pydantic import BaseModel

from ..models.country_code import CountryCode
from ..models.uuid import Uuid


class NewAddress(BaseModel):
    """The struct that is used to create a new record. This is automatically generated and has all the same fields as the main struct only it is missing the `id`."""

    city: Optional[str] = None

    country: CountryCode

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    user_id: Uuid

    zip: Optional[str] = None
