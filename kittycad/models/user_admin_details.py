from typing import List, Optional

from ..models.address import Address
from ..models.block_reason import BlockReason
from ..models.payment_method import PaymentMethod
from ..models.user_cad_info_admin_details import UserCadInfoAdminDetails
from .base import KittyCadBaseModel


class UserAdminDetails(KittyCadBaseModel):
    """Extra admin-only details for a user."""

    active_api_tokens_count: int

    active_device_tokens_count: int

    active_sessions_count: int

    address: Optional[Address] = None

    address_summary: Optional[str] = None

    block: Optional[BlockReason] = None

    block_message: Optional[str] = None

    cad_user_info: Optional[UserCadInfoAdminDetails] = None

    hubspot_contact_url: Optional[str] = None

    payment_methods: List[PaymentMethod]

    payment_methods_summary: List[str]

    stripe_customer_id: Optional[str] = None

    stripe_dashboard_url: Optional[str] = None
