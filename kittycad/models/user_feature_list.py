from typing import List

from ..models.user_feature_entry import UserFeatureEntry
from .base import KittyCadBaseModel


class UserFeatureList(KittyCadBaseModel):
    """User features response payload."""

    features: List[UserFeatureEntry]
