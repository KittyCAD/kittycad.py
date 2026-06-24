from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgSkillResponse(KittyCadBaseModel):
    """Public skill context available to the caller's organization."""

    description: str

    id: Uuid

    markdown: str

    name: str
