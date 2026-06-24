from typing import Optional

from ..models.org_dataset_source import OrgDatasetSource
from .base import KittyCadBaseModel


class CreateOrgDataset(KittyCadBaseModel):
    """Payload for creating an org dataset."""

    description: Optional[str] = None

    name: str

    require_raw_kcl_similarity_score_for_success: Optional[bool] = False

    source: OrgDatasetSource
