from typing import Optional

from ..models.project_access_scope import ProjectAccessScope
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectAccessResponse(KittyCadBaseModel):
    """Effective capabilities for an authenticated project response."""

    can_delete: bool

    can_edit: bool

    organization_id: Optional[Uuid] = None

    scope: ProjectAccessScope
