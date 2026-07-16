from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryJobResponse(KittyCadBaseModel):
    """Response returned when a Factory job is created. Only customer-facing ids are exposed: the job id (the customer's reference) and its current version id. The internal Help Desk thread id is deliberately NOT returned (internal-only per the ERD)."""

    current_version_id: Optional[Uuid] = None

    id: Uuid

    status: str
