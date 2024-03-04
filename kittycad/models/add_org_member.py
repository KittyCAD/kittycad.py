
from pydantic import BaseModel, ConfigDict

from ..models.user_org_role import UserOrgRole


class AddOrgMember(BaseModel):
    """Data for adding a member to an org."""

    email: str

    role: UserOrgRole

    model_config = ConfigDict(protected_namespaces=())
