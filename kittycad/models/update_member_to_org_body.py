from ..models.user_org_role import UserOrgRole
from .base import KittyCadBaseModel


class UpdateMemberToOrgBody(KittyCadBaseModel):
    """Data for updating a member of an org."""

    role: UserOrgRole
