from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.country_code import CountryCode


class IpAddrInfo(BaseModel):
    """Information about an ip address. Represents geographical and network-related information."""

    asn: Optional[int] = None

    city: Optional[str] = None

    continent_code: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[CountryCode] = None

    country_code3: Optional[str] = None

    ip: Optional[str] = None

    is_in_european_union: Optional[bool] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    offset: Optional[int] = None

    organization: Optional[str] = None

    postal_code: Optional[str] = None

    region: Optional[str] = None

    region_code: Optional[str] = None

    timezone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
