from ..models.kcl_project_share_link_access_mode import KclProjectShareLinkAccessMode
from .base import KittyCadBaseModel


class CreateProjectShareLinkRequest(KittyCadBaseModel):
    """Request payload for creating a new project share link."""

    access_mode: KclProjectShareLinkAccessMode = "anyone_with_link"  # type: ignore[assignment]
