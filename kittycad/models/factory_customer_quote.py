import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryCustomerQuote(KittyCadBaseModel):
    """Customer prices only. Internal costs and worksheet notes never enter this type."""

    delivery_estimate: str

    estimated_delivery_business_days: Optional[int] = None

    expires_at: datetime.datetime

    id: Uuid

    is_expedited: bool

    job_version_id: Uuid

    part_quantity: Optional[int] = None

    price_per_part_cents: Optional[int] = None

    published_at: datetime.datetime

    shipping_cents: int

    subtotal_cents: int

    total_before_tax_cents: int
