
from pydantic import BaseModel, ConfigDict

from ..models.org_role import OrgRole


class UpdateMemberToOrgBody(BaseModel):
    """Data for updating a member of an org."""

    role: OrgRole

    model_config = ConfigDict(protected_namespaces=())
