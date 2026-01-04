from ..models.storage_provider import StorageProvider
from .base import KittyCadBaseModel


class OrgDatasetSource(KittyCadBaseModel):
    """Details for accessing an org dataset."""

    access_role_arn: str

    provider: StorageProvider

    uri: str
