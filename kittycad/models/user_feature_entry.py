from ..models.user_feature import UserFeature
from .base import KittyCadBaseModel


class UserFeatureEntry(KittyCadBaseModel):
    """Enabled features surfaced to end users."""

    id: UserFeature
