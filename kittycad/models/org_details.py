from typing import Optional

from pydantic import BaseModel, ConfigDict



class OrgDetails(BaseModel):
    """The user-modifiable parts of an organization."""

    allow_users_in_domain_to_auto_join: Optional[bool] = None

    billing_email: Optional[str] = None

    domain: Optional[str] = None

    image: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
