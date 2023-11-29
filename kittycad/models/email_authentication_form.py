from typing import Optional

from pydantic import BaseModel



class EmailAuthenticationForm(BaseModel):
    """The body of the form for email authentication."""

    callback_url: Optional[str] = None

    email: str
