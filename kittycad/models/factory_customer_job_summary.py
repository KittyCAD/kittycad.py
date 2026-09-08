import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryCustomerJobSummary(KittyCadBaseModel):
    """Customer-visible summary of a manufacturing job."""

    created_at: datetime.datetime

    current_version_id: Optional[Uuid] = None

    id: Uuid

    status: str

    updated_at: datetime.datetime
