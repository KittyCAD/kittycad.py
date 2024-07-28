import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.jetstream_api_stats import JetstreamApiStats
from .base64data import Base64Data


class JetstreamStats(BaseModel):
    """Jetstream statistics."""

    accounts: Optional[int] = None

    api: Optional[JetstreamApiStats] = None

    ha_assets: Optional[int] = None

    memory: Optional[int] = None

    reserved_memory: Optional[int] = None

    reserved_store: Optional[int] = None

    store: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
