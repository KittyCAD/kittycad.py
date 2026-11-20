from typing import Optional

from ..models.address_content import AddressContent
from ..models.factory_customer_job_summary import FactoryCustomerJobSummary
from ..models.factory_customer_job_version import FactoryCustomerJobVersion
from ..models.factory_customer_quote import FactoryCustomerQuote
from .base import KittyCadBaseModel


class FactoryCustomerJobDetail(KittyCadBaseModel):
    """Customer-visible detail for a single Factory job."""

    current_version: Optional[FactoryCustomerJobVersion] = None

    is_expedited: bool

    job: FactoryCustomerJobSummary

    quote: Optional[FactoryCustomerQuote] = None

    shipping_info: Optional[AddressContent] = None
