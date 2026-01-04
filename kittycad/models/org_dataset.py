import datetime
from typing import Optional

from ..models.org_dataset_status import OrgDatasetStatus
from ..models.storage_provider import StorageProvider
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDataset(KittyCadBaseModel):
    """Dataset owned by an organization, reusable across multiple features."""

    access_role_arn: str

    created_at: datetime.datetime

    id: Uuid

    last_sync_error: Optional[str] = None

    last_sync_error_at: Optional[datetime.datetime] = None

    name: str

    org_id: Uuid

    source_uri: str

    status: OrgDatasetStatus

    storage_provider: StorageProvider

    updated_at: datetime.datetime
