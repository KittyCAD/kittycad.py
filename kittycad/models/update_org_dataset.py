from typing import Optional

from ..models.update_org_dataset_source import UpdateOrgDatasetSource
from .base import KittyCadBaseModel


class UpdateOrgDataset(KittyCadBaseModel):
    """Payload for updating an org dataset."""

    name: Optional[str] = None

    source: Optional[UpdateOrgDatasetSource] = None
