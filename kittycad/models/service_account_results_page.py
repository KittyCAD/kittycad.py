import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.service_account import ServiceAccount
from .base64data import Base64Data


class ServiceAccountResultsPage(BaseModel):
    """A single page of results"""

    items: List[ServiceAccount]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
