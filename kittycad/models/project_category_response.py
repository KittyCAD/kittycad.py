from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectCategoryResponse(KittyCadBaseModel):
    """Active category metadata available for project submission flows."""

    description: str

    display_name: str

    id: Uuid

    slug: str

    sort_order: int
