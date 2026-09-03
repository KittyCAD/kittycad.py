from .base import KittyCadBaseModel


class MlCopilotProjectRevision(KittyCadBaseModel):
    """Canonical project revision accepted by API."""

    project_id: str

    revision: str

    writer_fence: str
