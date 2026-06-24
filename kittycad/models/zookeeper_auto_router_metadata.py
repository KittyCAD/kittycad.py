from typing import List, Optional

from .base import KittyCadBaseModel


class ZookeeperAutoRouterMetadata(KittyCadBaseModel):
    """Zookeeper Auto-router decision metadata persisted on a copilot prompt."""

    bucket: str

    prompt_template: Optional[str] = None

    reasons: Optional[List[str]] = None

    stage: Optional[str] = None
