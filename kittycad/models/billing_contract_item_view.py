from typing import List, Optional

from ..models.billing_item_code import BillingItemCode
from ..models.billing_item_kind import BillingItemKind
from ..models.billing_rate_tier_view import BillingRateTierView
from ..models.billing_unit import BillingUnit
from ..models.billing_unit_granularity import BillingUnitGranularity
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class BillingContractItemView(KittyCadBaseModel):
    """Serialized line item returned from a stored contract."""

    active: bool

    billing_unit_granularity: Optional[BillingUnitGranularity] = None

    code: BillingItemCode

    display_name: str

    fixed_fee_amount: Optional[float] = None

    id: Uuid

    is_commitment_eligible: bool

    kind: BillingItemKind

    rate_tiers: List[BillingRateTierView]

    unit: BillingUnit
