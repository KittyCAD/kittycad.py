from ..models.org_dataset_source import OrgDatasetSource
from .base import KittyCadBaseModel


class CreateOrgDataset(KittyCadBaseModel):
    """Payload for creating an org dataset."""

    name: str

    source: OrgDatasetSource
