from typing import Optional

from pydantic import BaseModel, ConfigDict


class CreateShortlinkRequest(BaseModel):
    """Request to create a shortlink."""

    password: Optional[str] = None

    restrict_to_org: bool = False

    url: str

    model_config = ConfigDict(protected_namespaces=())
