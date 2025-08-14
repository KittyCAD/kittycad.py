from typing import Optional

from pydantic import BaseModel, ConfigDict


class UpdateShortlinkRequest(BaseModel):
    """Request to update a shortlink."""

    password: Optional[str] = None

    restrict_to_org: bool

    model_config = ConfigDict(protected_namespaces=())
