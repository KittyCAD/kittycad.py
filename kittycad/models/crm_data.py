from typing import Optional

from pydantic import BaseModel, ConfigDict


class CrmData(BaseModel):
    """The data for subscribing a user to the newsletter."""

    cad_industry: Optional[str] = None

    cad_user_type: Optional[str] = None

    number_of_cad_users: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
