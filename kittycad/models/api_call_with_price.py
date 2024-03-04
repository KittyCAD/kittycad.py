import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.method import Method
from ..models.uuid import Uuid


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
