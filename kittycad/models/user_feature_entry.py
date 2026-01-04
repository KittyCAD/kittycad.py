from .base import KittyCadBaseModel


class UserFeatureEntry(KittyCadBaseModel):
    """Enabled features surfaced to end users."""

    id: str
