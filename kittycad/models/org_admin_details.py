from typing import List, Optional

from ..models.block_reason import BlockReason
from ..models.org_address import OrgAddress
from ..models.payment_method import PaymentMethod
from .base import KittyCadBaseModel


class OrgAdminDetails(KittyCadBaseModel):
    """Extra admin-only details for an organization."""

    address: Optional[OrgAddress] = None

    address_summary: Optional[str] = None

    block: Optional[BlockReason] = None

    block_message: Optional[str] = None

    payment_methods: List[PaymentMethod]

    payment_methods_summary: List[str]

    stripe_customer_id: Optional[str] = None

    stripe_dashboard_url: Optional[str] = None
