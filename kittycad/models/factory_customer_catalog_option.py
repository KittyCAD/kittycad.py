from .base import KittyCadBaseModel


class FactoryCustomerCatalogOption(KittyCadBaseModel):
    """One customer-selectable Factory catalog entry."""

    name: str
