from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.org_member import OrgMember


class Orgmemberresultspage(BaseModel):
    """A single page of results"""

    items: List[OrgMember]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
