from typing import Optional

from .base import KittyCadBaseModel


class UpdateUser(KittyCadBaseModel):
    """The user-modifiable parts of a User."""

    company: Optional[str] = None

    discord: Optional[str] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    image: str

    is_onboarded: Optional[bool] = None

    last_name: Optional[str] = None

    phone: str = ""
