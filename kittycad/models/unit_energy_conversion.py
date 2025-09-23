import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.unit_energy import UnitEnergy
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class UnitEnergyConversion(KittyCadBaseModel):
    """Result of converting between units."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    input: float = 0.0

    input_unit: UnitEnergy

    output: Optional[float] = None

    output_unit: UnitEnergy

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
