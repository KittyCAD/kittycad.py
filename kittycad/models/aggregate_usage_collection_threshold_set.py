from .base import KittyCadBaseModel


class AggregateUsageCollectionThresholdSet(KittyCadBaseModel):
    """An explicit collection-threshold value to configure for an account."""

    amount: float

    expected_version: int
