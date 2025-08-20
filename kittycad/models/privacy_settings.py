from .base import KittyCadBaseModel


class PrivacySettings(KittyCadBaseModel):
    """Privacy settings for an org or user."""

    can_train_on_data: bool
