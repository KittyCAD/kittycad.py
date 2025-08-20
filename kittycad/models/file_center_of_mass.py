import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.file_import_format import FileImportFormat
from ..models.point3d import Point3d
from ..models.unit_length import UnitLength
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FileCenterOfMass(KittyCadBaseModel):
    """A file center of mass result."""

    center_of_mass: Optional[Point3d] = None

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
