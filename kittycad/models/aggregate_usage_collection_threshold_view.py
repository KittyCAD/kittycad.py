from typing import Optional

from ..models.aggregate_usage_collection_threshold_bounds import (
    AggregateUsageCollectionThresholdBounds,
)
from ..models.aggregate_usage_collection_threshold_source import (
    AggregateUsageCollectionThresholdSource,
)
from .base import KittyCadBaseModel


class AggregateUsageCollectionThresholdView(KittyCadBaseModel):
    """Configured and effective aggregate-usage collection-threshold state."""

    admin_amount: Optional[float] = None

    admin_bounds: AggregateUsageCollectionThresholdBounds

    customer_amount: Optional[float] = None

    customer_bounds: AggregateUsageCollectionThresholdBounds

    default_amount: float

    effective_amount: float

    source: AggregateUsageCollectionThresholdSource

    version: int
