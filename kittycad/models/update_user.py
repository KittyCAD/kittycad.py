from typing import Optional

from pydantic import BaseModel



class UpdateUser(BaseModel):
    """The user-modifiable parts of a User."""

    company: Optional[str] = None

    discord: Optional[str] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    last_name: Optional[str] = None

    phone: Optional[str] = None
