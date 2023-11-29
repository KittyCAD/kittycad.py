import datetime
from typing import Optional

from pydantic import BaseModel

from ..models.api_call_status import ApiCallStatus
from ..models.unit_force import UnitForce
from ..models.uuid import Uuid


class UnitForceConversion(BaseModel):
    """Result of converting between units."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    input: Optional[float] = None

    input_unit: UnitForce

    output: Optional[float] = None

    output_unit: UnitForce

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
