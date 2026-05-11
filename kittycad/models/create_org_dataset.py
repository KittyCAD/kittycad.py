from typing import Optional

from ..models.org_dataset_source import OrgDatasetSource
from .base import KittyCadBaseModel


class CreateOrgDataset(KittyCadBaseModel):
    """Payload for creating an org dataset."""

    description: Optional[str] = None

    name: str

    source: OrgDatasetSource
