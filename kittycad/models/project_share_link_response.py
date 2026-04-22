import datetime

from ..models.kcl_project_share_link_access_mode import KclProjectShareLinkAccessMode
from .base import KittyCadBaseModel


class ProjectShareLinkResponse(KittyCadBaseModel):
    """Owner-visible share-link metadata for project downloads."""

    access_mode: KclProjectShareLinkAccessMode

    created_at: datetime.datetime

    key: str

    updated_at: datetime.datetime

    url: str
