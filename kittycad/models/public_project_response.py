import datetime
from typing import List, Optional

from ..models.project_category_response import ProjectCategoryResponse
from ..models.public_project_owner_response import PublicProjectOwnerResponse
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class PublicProjectResponse(KittyCadBaseModel):
    """Public community project metadata for gallery listings."""

    categories: List[ProjectCategoryResponse]

    description: str

    id: Uuid

    like_count: int

    liked: Optional[bool] = None

    owner: PublicProjectOwnerResponse

    preview_url: Optional[str] = None

    published_at: datetime.datetime

    title: str
