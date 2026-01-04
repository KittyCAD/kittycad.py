from typing import Optional

from ..models.storage_provider import StorageProvider
from .base import KittyCadBaseModel


class UpdateOrgDatasetSource(KittyCadBaseModel):
    """Partial update payload for dataset storage details."""

    access_role_arn: Optional[str] = None

    provider: Optional[StorageProvider] = None

    uri: Optional[str] = None
