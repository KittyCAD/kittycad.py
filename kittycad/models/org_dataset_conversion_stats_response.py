from typing import Dict

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDatasetConversionStatsResponse(KittyCadBaseModel):
    """Summary statistics for an org dataset's conversions."""

    by_status: Dict[str, int]

    dataset_id: Uuid

    failures: int

    successes: int

    total: int
