import datetime
from typing import Any, List, Optional

from ..models.org_dataset_file_conversion_phase import OrgDatasetFileConversionPhase
from ..models.org_dataset_file_conversion_status import OrgDatasetFileConversionStatus
from ..models.org_dataset_snapshot_image import OrgDatasetSnapshotImage
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDatasetFileConversionDetails(KittyCadBaseModel):
    """Detailed response that bundles conversion metadata with converted file and snapshot contents."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    dataset_id: Uuid

    file_etag: str

    file_path: str

    file_size: int

    id: Uuid

    importer_version: Optional[str] = None

    metadata: Optional[Any] = None

    original_snapshot_images: List[OrgDatasetSnapshotImage]

    output: Optional[str] = None

    phase: OrgDatasetFileConversionPhase

    raw_kcl_output: Optional[str] = None

    raw_kcl_snapshot_images: List[OrgDatasetSnapshotImage]

    salon_kcl_output: Optional[str] = None

    salon_kcl_snapshot_images: List[OrgDatasetSnapshotImage]

    started_at: Optional[datetime.datetime] = None

    status: OrgDatasetFileConversionStatus

    status_message: Optional[str] = None

    updated_at: datetime.datetime
