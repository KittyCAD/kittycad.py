import datetime
from typing import List, Optional

from ..models.billing_cadence import BillingCadence
from ..models.billing_commitment_scope import BillingCommitmentScope
from ..models.billing_contract_item_input import BillingContractItemInput
from ..models.billing_contract_status import BillingContractStatus
from ..models.billing_external_customer_id import BillingExternalCustomerId
from ..models.billing_period_input import BillingPeriodInput
from ..models.billing_provider import BillingProvider
from ..models.billing_rollover_policy import BillingRolloverPolicy
from ..models.currency import Currency
from .base import KittyCadBaseModel


class BillingContractUpsert(KittyCadBaseModel):
    """Complete contract payload used to create or replace an org's contract."""

    billing_cadence: BillingCadence

    commitment_scope: BillingCommitmentScope

    currency: Currency

    discount_description: Optional[str] = None

    effective_at: datetime.datetime

    external_customer_id: Optional[BillingExternalCustomerId] = None

    items: List[BillingContractItemInput]

    name: str

    notes: Optional[str] = None

    periods: List[BillingPeriodInput]

    provider: BillingProvider

    rollover_policy: BillingRolloverPolicy

    status: BillingContractStatus

    term_end_at: datetime.datetime
