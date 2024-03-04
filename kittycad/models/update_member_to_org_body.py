
from pydantic import BaseModel, ConfigDict

from ..models.user_org_role import UserOrgRole


class UpdateMemberToOrgBody(BaseModel):
    """Data for updating a member of an org."""

    role: UserOrgRole

    model_config = ConfigDict(protected_namespaces=())
