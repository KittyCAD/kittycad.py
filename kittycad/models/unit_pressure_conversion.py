import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.unit_pressure import UnitPressure
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class UnitPressureConversion(KittyCadBaseModel):
    """Result of converting between units."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    input: float = 0.0

    input_unit: UnitPressure

    output: Optional[float] = None

    output_unit: UnitPressure

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
