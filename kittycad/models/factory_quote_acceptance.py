from ..models.factory_customer_job_summary import FactoryCustomerJobSummary
from ..models.invoice import Invoice
from .base import KittyCadBaseModel


class FactoryQuoteAcceptance(KittyCadBaseModel):
    """A paid invoice and the manufacturing job it releases for production."""

    invoice: Invoice

    job: FactoryCustomerJobSummary
