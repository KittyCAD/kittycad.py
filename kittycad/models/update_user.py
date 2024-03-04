from typing import Optional

from pydantic import BaseModel, ConfigDict



class UpdateUser(BaseModel):
    """The user-modifiable parts of a User."""

    company: Optional[str] = None

    discord: Optional[str] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    image: str

    last_name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
