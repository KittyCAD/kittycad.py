import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.file_import_format import FileImportFormat
from ..models.unit_area import UnitArea
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FileSurfaceArea(KittyCadBaseModel):
    """A file surface area result."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_unit: UnitArea

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    surface_area: Optional[float] = None

    updated_at: datetime.datetime

    user_id: Uuid
