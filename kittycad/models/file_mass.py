import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.file_import_format import FileImportFormat
from ..models.unit_density import UnitDensity
from ..models.unit_mass import UnitMass
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FileMass(KittyCadBaseModel):
    """A file mass result."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    mass: Optional[float] = None

    material_density: float = 0.0

    material_density_unit: UnitDensity

    output_unit: UnitMass

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
