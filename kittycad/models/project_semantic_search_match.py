from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectSemanticSearchMatch(KittyCadBaseModel):
    """One matching current project, rather than one match for every source file."""

    description: str

    project_id: Uuid

    similarity: float

    title: str

    version_id: Uuid
