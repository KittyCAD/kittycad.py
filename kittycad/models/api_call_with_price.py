import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.method import Method
from ..models.uuid import Uuid
from .base64data import Base64Data


class ApiCallWithPrice(BaseModel):
    """An API call with the price.

    This is a join of the `ApiCall` and `ApiCallPrice` tables."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    duration: Optional[int] = None

    email: Optional[str] = None

    endpoint: Optional[str] = None

    id: Uuid

    ip_address: Optional[str] = None

    litterbox: Optional[bool] = None

    method: Method

    minutes: Optional[int] = None

    org_id: Optional[Uuid] = None

    origin: Optional[str] = None

    price: Optional[float] = None

    request_body: Optional[str] = None

    request_query_params: Optional[str] = None

    response_body: Optional[str] = None

    started_at: Optional[datetime.datetime] = None

    status_code: Optional[int] = None

    stripe_invoice_item_id: Optional[str] = None

    token: Uuid

    updated_at: datetime.datetime

    user_agent: str

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
