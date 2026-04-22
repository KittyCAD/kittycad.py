import datetime
from typing import List, Optional

from ..models.billing_cadence import BillingCadence
from ..models.billing_commitment_scope import BillingCommitmentScope
from ..models.billing_contract_item_view import BillingContractItemView
from ..models.billing_contract_status import BillingContractStatus
from ..models.billing_external_customer_id import BillingExternalCustomerId
from ..models.billing_period_view import BillingPeriodView
from ..models.billing_provider import BillingProvider
from ..models.billing_rollover_policy import BillingRolloverPolicy
from ..models.currency import Currency
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class BillingContractView(KittyCadBaseModel):
    """Serialized contract snapshot returned from the database."""

    account_id: Uuid

    billing_cadence: BillingCadence

    commitment_scope: BillingCommitmentScope

    contract_id: Uuid

    currency: Currency

    discount_description: Optional[str] = None

    effective_at: datetime.datetime

    external_customer_id: Optional[BillingExternalCustomerId] = None

    items: List[BillingContractItemView]

    name: str

    notes: Optional[str] = None

    periods: List[BillingPeriodView]

    provider: BillingProvider

    rollover_policy: BillingRolloverPolicy

    status: BillingContractStatus

    term_end_at: datetime.datetime
