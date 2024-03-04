import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.unit_area import UnitArea
from ..models.uuid import Uuid


class UnitAreaConversion(BaseModel):
    """Result of converting between units."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    input: Optional[float] = None

    input_unit: UnitArea

    output: Optional[float] = None

    output_unit: UnitArea

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
