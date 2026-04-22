from typing import List, Optional

from ..models.billing_item_code import BillingItemCode
from ..models.billing_item_kind import BillingItemKind
from ..models.billing_rate_tier_input import BillingRateTierInput
from ..models.billing_unit import BillingUnit
from ..models.billing_unit_granularity import BillingUnitGranularity
from .base import KittyCadBaseModel


class BillingContractItemInput(KittyCadBaseModel):
    """Serialized line-item payload for a contract definition."""

    active: bool = True

    billing_unit_granularity: Optional[BillingUnitGranularity] = None

    code: BillingItemCode

    display_name: str

    fixed_fee_amount: Optional[float] = None

    is_commitment_eligible: bool = False

    kind: BillingItemKind

    rate_tiers: List[BillingRateTierInput] = []

    unit: BillingUnit
