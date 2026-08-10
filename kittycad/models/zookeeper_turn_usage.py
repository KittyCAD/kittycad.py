from typing import List, Optional

from ..models.zookeeper_turn_usage_model import ZookeeperTurnUsageModel
from ..models.zookeeper_turn_usage_stage import ZookeeperTurnUsageStage
from .base import KittyCadBaseModel


class ZookeeperTurnUsage(KittyCadBaseModel):
    """Token usage and cost for one completed Zookeeper turn.

    A turn is many model calls: the streamed agent loop, helper agents, conversation compaction, Auto-mode routing, and any retried attempts. This is the sum of all of them, with breakdowns by model and by stage."""

    api_call_id: Optional[str] = None

    cache_write_input_tokens: Optional[int] = 0

    cached_input_tokens: Optional[int] = 0

    conversation_id: Optional[str] = None

    cost_micro_usd: Optional[int] = 0

    cost_usd: Optional[str] = ""

    fully_priced: Optional[bool] = False

    input_tokens: Optional[int] = 0

    models: Optional[List[ZookeeperTurnUsageModel]] = None

    output_tokens: Optional[int] = 0

    priced_requests: Optional[int] = 0

    reasoning_tokens: Optional[int] = 0

    requests: Optional[int] = 0

    schema_version: Optional[str] = ""

    stages: Optional[List[ZookeeperTurnUsageStage]] = None

    total_tokens: Optional[int] = 0

    uncached_input_tokens: Optional[int] = 0

    unpriced_requests: Optional[int] = 0
