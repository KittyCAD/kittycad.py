from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.country_code import CountryCode


class AddressDetails(BaseModel):
    """Address details."""

    city: Optional[str] = None

    country: CountryCode

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    zip: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
