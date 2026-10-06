from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class CreateProjectVersionResponse(KittyCadBaseModel):
    """Result of saving an alternate project version."""

    current_version_id: Uuid

    version_id: Uuid
