import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.file_import_format import FileImportFormat
from ..models.unit_density import UnitDensity
from ..models.unit_mass import UnitMass
from ..models.uuid import Uuid


class FileDensity(BaseModel):
    """A file density result."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    density: Optional[float] = None

    error: Optional[str] = None

    id: Uuid

    material_mass: Optional[float] = None

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
