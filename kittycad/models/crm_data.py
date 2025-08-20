from typing import Optional

from .base import KittyCadBaseModel


class CrmData(KittyCadBaseModel):
    """The data for subscribing a user to the newsletter."""

    cad_industry: Optional[str] = None

    cad_user_type: Optional[str] = None

    number_of_cad_users: Optional[str] = None
