import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.bounding_box import BoundingBox
from ..models.file_import_format import FileImportFormat
from ..models.unit_length import UnitLength
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FileBoundingBox(KittyCadBaseModel):
    """A file bounding box result."""

    bounding_box: Optional[BoundingBox] = None

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_unit: UnitLength

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
