import datetime
from typing import Any, Optional

from ..models.org_dataset_file_conversion_phase import OrgDatasetFileConversionPhase
from ..models.org_dataset_file_conversion_status import OrgDatasetFileConversionStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDatasetFileConversionSummary(KittyCadBaseModel):
    """Publicly exposed view of a dataset file conversion that omits storage-specific fields."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    dataset_id: Uuid

    file_etag: str

    file_path: str

    file_size: int

    id: Uuid

    importer_version: Optional[str] = None

    manual_kcl_override_active: bool

    manual_kcl_override_updated_at: Optional[datetime.datetime] = None

    metadata: Optional[Any] = None

    phase: OrgDatasetFileConversionPhase

    raw_kcl_similarity_score: Optional[float] = None

    salon_kcl_similarity_score: Optional[float] = None

    started_at: Optional[datetime.datetime] = None

    status: OrgDatasetFileConversionStatus

    status_message: Optional[str] = None

    updated_at: datetime.datetime
