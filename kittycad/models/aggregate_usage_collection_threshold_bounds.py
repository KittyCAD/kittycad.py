from .base import KittyCadBaseModel


class AggregateUsageCollectionThresholdBounds(KittyCadBaseModel):
    """Inclusive amount bounds for a threshold authority."""

    maximum_amount: float

    minimum_amount: float
