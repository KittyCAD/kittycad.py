from typing import Optional

from .base import KittyCadBaseModel


class CreateShortlinkRequest(KittyCadBaseModel):
    """Request to create a shortlink."""

    password: Optional[str] = None

    restrict_to_org: bool = False

    url: str
