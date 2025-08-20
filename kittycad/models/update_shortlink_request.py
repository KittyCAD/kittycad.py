from typing import Optional

from .base import KittyCadBaseModel


class UpdateShortlinkRequest(KittyCadBaseModel):
    """Request to update a shortlink."""

    password: Optional[str] = None

    restrict_to_org: bool
