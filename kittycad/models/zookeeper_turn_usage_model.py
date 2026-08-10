from typing import Optional

from .base import KittyCadBaseModel


class ZookeeperTurnUsageModel(KittyCadBaseModel):
    """Per-model usage within a Zookeeper turn."""

    cache_write_input_tokens: Optional[int] = 0

    cached_input_tokens: Optional[int] = 0

    cost_micro_usd: Optional[int] = 0

    cost_usd: Optional[str] = ""

    fully_priced: Optional[bool] = False

    input_tokens: Optional[int] = 0

    model: str

    output_tokens: Optional[int] = 0

    priced_requests: Optional[int] = 0

    pricing_source: Optional[str] = ""

    reasoning_tokens: Optional[int] = 0

    requests: Optional[int] = 0

    total_tokens: Optional[int] = 0

    uncached_input_tokens: Optional[int] = 0

    unpriced_requests: Optional[int] = 0
