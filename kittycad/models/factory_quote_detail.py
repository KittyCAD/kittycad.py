from ..models.factory_customer_quote import FactoryCustomerQuote
from ..models.factory_quote_preview import FactoryQuotePreview
from .base import KittyCadBaseModel


class FactoryQuoteDetail(KittyCadBaseModel):
    """A published customer offer and its current checkout amounts."""

    pricing: FactoryQuotePreview

    quote: FactoryCustomerQuote
