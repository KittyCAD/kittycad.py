
from pydantic import BaseModel, ConfigDict

from ..models.org_role import OrgRole


class AddOrgMember(BaseModel):
    """Data for adding a member to an org."""

    email: str

    role: OrgRole

    model_config = ConfigDict(protected_namespaces=())
