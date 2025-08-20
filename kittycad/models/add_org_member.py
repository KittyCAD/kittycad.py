from ..models.user_org_role import UserOrgRole
from .base import KittyCadBaseModel


class AddOrgMember(KittyCadBaseModel):
    """Data for adding a member to an org."""

    email: str

    role: UserOrgRole
