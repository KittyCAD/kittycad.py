from typing import Optional

from .base import KittyCadBaseModel


class EmailAuthenticationForm(KittyCadBaseModel):
    """The body of the form for email authentication."""

    callback_url: Optional[str] = None

    email: str
