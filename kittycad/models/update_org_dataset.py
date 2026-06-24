from typing import Optional

from ..models.update_org_dataset_source import UpdateOrgDatasetSource
from .base import KittyCadBaseModel


class UpdateOrgDataset(KittyCadBaseModel):
    """Payload for updating an org dataset."""

    description: Optional[str] = None

    name: Optional[str] = None

    require_raw_kcl_similarity_score_for_success: Optional[bool] = None

    source: Optional[UpdateOrgDatasetSource] = None
