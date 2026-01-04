import datetime
from typing import Optional

from ..models.org_dataset_file_conversion_status import OrgDatasetFileConversionStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDatasetFileConversion(KittyCadBaseModel):
    """Tracks state of `OrgDataset` file conversions."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    dataset_id: Uuid

    file_etag: str

    file_path: str

    file_size: int

    id: Uuid

    importer_version: Optional[str] = None

    output_path: Optional[str] = None

    started_at: Optional[datetime.datetime] = None

    status: OrgDatasetFileConversionStatus

    status_message: Optional[str] = None

    updated_at: datetime.datetime
