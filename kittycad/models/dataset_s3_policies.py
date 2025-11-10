from typing import Any

from .base import KittyCadBaseModel


class DatasetS3Policies(KittyCadBaseModel):
    """Aggregated AWS policies required for onboarding an org dataset stored in S3."""

    bucket_policy: Any

    permission_policy: Any

    trust_policy: Any
